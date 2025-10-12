"""Example script demonstrating how to create a periodic automation task."""

from houseelf.base_script import BaseScript


class ExampleScript(BaseScript):
    """Example script that demonstrates the BaseScript usage.
    
    This is a simple example that logs messages and returns a result.
    Replace this with your actual automation logic.
    """
    
    def __init__(self):
        """Initialize the example script."""
        super().__init__(name="ExampleScript")
    
    def run(self) -> str:
        """Execute the example script logic.
        
        Returns:
            A success message
        """
        self.logger.info("Performing example task...")
        
        # Your automation logic goes here
        # For example:
        # - Fetch data from an API
        # - Process files
        # - Update databases
        # - Send notifications
        # etc.
        
        self.logger.info("Task step 1: Complete")
        self.logger.info("Task step 2: Complete")
        self.logger.info("Task step 3: Complete")
        
        return "Example task completed successfully"


def main():
    """Main entry point for the script."""
    script = ExampleScript()
    exit_code = script.execute()
    exit(exit_code)


if __name__ == "__main__":
    main()
