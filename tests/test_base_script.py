"""Tests for the BaseScript class."""

import logging
from unittest.mock import patch

import pytest

from houseelf.base_script import BaseScript


class SimpleScript(BaseScript):
    """A simple test script."""

    def __init__(self):
        super().__init__(name="SimpleScript")

    def run(self):
        """Simple run implementation."""
        self.logger.info("Running simple script")
        return "success"


class FailingScript(BaseScript):
    """A script that always fails."""

    def __init__(self):
        super().__init__(name="FailingScript")

    def run(self):
        """Run implementation that raises an error."""
        raise ValueError("Intentional error for testing")


def test_base_script_initialization():
    """Test that BaseScript initializes correctly."""
    script = SimpleScript()
    assert script.name == "SimpleScript"
    assert isinstance(script.logger, logging.Logger)


def test_base_script_execute_success():
    """Test successful script execution."""
    script = SimpleScript()
    exit_code = script.execute()
    assert exit_code == 0


def test_base_script_execute_failure():
    """Test script execution with failure."""
    script = FailingScript()
    exit_code = script.execute()
    assert exit_code == 1


def test_base_script_logger_output(caplog):
    """Test that logger outputs correctly."""
    script = SimpleScript()
    with caplog.at_level(logging.INFO):
        result = script.run()
    
    assert result == "success"
    assert "Running simple script" in caplog.text


def test_base_script_custom_name():
    """Test BaseScript with custom name."""
    
    class CustomNameScript(BaseScript):
        def __init__(self):
            super().__init__(name="CustomName")
        
        def run(self):
            return "done"
    
    script = CustomNameScript()
    assert script.name == "CustomName"


def test_base_script_log_level():
    """Test BaseScript with custom log level."""
    
    class DebugScript(BaseScript):
        def __init__(self):
            super().__init__(log_level=logging.DEBUG)
        
        def run(self):
            return "done"
    
    script = DebugScript()
    assert script.logger.level == logging.DEBUG
