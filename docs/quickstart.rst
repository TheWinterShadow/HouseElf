Quick Start
===========

Installation
------------

Install HouseElf using pip:

.. code-block:: bash

    pip install -e .

Or for development:

.. code-block:: bash

    pip install -e ".[dev]"

Creating Your First Script
---------------------------

1. Create a new Python file in ``src/houseelf/scripts/`` directory:

.. code-block:: python

    from houseelf.base_script import BaseScript

    class MyScript(BaseScript):
        def __init__(self):
            super().__init__(name="MyScript")
        
        def run(self):
            self.logger.info("Starting my automation task...")
            # Your automation logic here
            return "Task completed successfully"
    
    def main():
        script = MyScript()
        exit_code = script.execute()
        exit(exit_code)
    
    if __name__ == "__main__":
        main()

2. Run your script:

.. code-block:: bash

    python -m houseelf.scripts.my_script

Running with Docker
-------------------

1. Build the Docker image:

.. code-block:: bash

    docker build -t houseelf:latest .

2. Run a specific script:

.. code-block:: bash

    docker run --rm houseelf:latest python -m houseelf.scripts.my_script

3. Run with environment variables:

.. code-block:: bash

    docker run --rm -e MY_VAR=value houseelf:latest python -m houseelf.scripts.my_script

Deploying to EC2
-----------------

1. Push your Docker image to ECR or Docker Hub
2. Use AWS EventBridge or cron to schedule periodic execution
3. Configure CloudWatch for log aggregation

Example crontab entry:

.. code-block:: bash

    # Run every day at 2 AM
    0 2 * * * docker run --rm houseelf:latest python -m houseelf.scripts.my_script
