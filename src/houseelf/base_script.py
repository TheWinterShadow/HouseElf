"""Base script class for periodic automation tasks."""

import logging
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class BaseScript(ABC):
    """Base class for all periodic automation scripts.
    
    This class provides a template for scripts that run periodically in Docker containers.
    Each script should inherit from this class and implement the `run` method.
    
    Attributes:
        name: The name of the script
        logger: Logger instance for the script
    """
    
    def __init__(self, name: str | None = None, log_level: int = logging.INFO):
        """Initialize the base script.
        
        Args:
            name: Optional name for the script. Defaults to class name.
            log_level: Logging level (default: INFO)
        """
        self.name = name or self.__class__.__name__
        self.logger = self._setup_logger(log_level)
        
    def _setup_logger(self, log_level: int) -> logging.Logger:
        """Setup logger with consistent formatting.
        
        Args:
            log_level: The logging level to use
            
        Returns:
            Configured logger instance
        """
        logger = logging.getLogger(self.name)
        logger.setLevel(log_level)
        
        # Create console handler with formatting
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        return logger
    
    @abstractmethod
    def run(self) -> Any:
        """Execute the main logic of the script.
        
        This method must be implemented by subclasses.
        
        Returns:
            Any result from the script execution
        """
        pass
    
    def execute(self) -> int:
        """Execute the script with error handling and logging.
        
        This method wraps the `run` method with standard logging and error handling.
        It should be called to execute the script from the command line.
        
        Returns:
            Exit code (0 for success, 1 for failure)
        """
        start_time = datetime.now()
        self.logger.info(f"Starting {self.name}")
        
        try:
            result = self.run()
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            self.logger.info(f"Completed {self.name} successfully in {duration:.2f} seconds")
            self.logger.info(f"Result: {result}")
            return 0
            
        except Exception as e:
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            self.logger.error(f"Failed to execute {self.name} after {duration:.2f} seconds")
            self.logger.error(f"Error: {str(e)}", exc_info=True)
            return 1
