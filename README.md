# HouseElf

> Daily automation tasks that run periodically in Docker containers

HouseElf is a Python package designed for running periodic automation tasks in Docker containers on EC2 instances. It provides a simple, structured framework for creating scripts that execute, log their output, and exit cleanly.

## Features

- 🐍 **Simple Base Class**: Easy-to-extend `BaseScript` class for all automation tasks
- 📝 **Built-in Logging**: Consistent logging format with timestamps and log levels
- 🐳 **Docker Ready**: Pre-configured Dockerfile for containerized execution
- ⚡ **Error Handling**: Automatic error catching and proper exit codes
- 📚 **Documentation**: Sphinx-based documentation with API reference
- 🧪 **Testing Ready**: Test structure following Python best practices
- 🔧 **Hatch Integration**: Modern Python project management with Hatch

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/TheWinterShadow/HouseElf.git
cd HouseElf

# Install with hatch
pip install hatch

# Install the package in development mode
pip install -e .
```

### Creating Your First Script

1. Create a new file in `src/houseelf/scripts/my_task.py`:

```python
from houseelf.base_script import BaseScript

class MyTask(BaseScript):
    def __init__(self):
        super().__init__(name="MyTask")
    
    def run(self):
        """Execute your automation logic here."""
        self.logger.info("Running my task...")
        # Your automation logic
        return "Task completed successfully"

def main():
    script = MyTask()
    exit_code = script.execute()
    exit(exit_code)

if __name__ == "__main__":
    main()
```

2. Run your script:

```bash
python -m houseelf.scripts.my_task
```

### Running with Docker

```bash
# Build the Docker image
docker build -t houseelf:latest .

# Run the example script
docker run --rm houseelf:latest python -m houseelf.scripts.example_script

# Run your custom script
docker run --rm houseelf:latest python -m houseelf.scripts.my_task
```

## Project Structure

```
HouseElf/
├── src/
│   └── houseelf/
│       ├── __init__.py           # Package initialization
│       ├── base_script.py        # Base class for all scripts
│       └── scripts/              # Your automation scripts
│           ├── __init__.py
│           └── example_script.py # Example implementation
├── tests/                        # Test files
├── docs/                         # Sphinx documentation
│   ├── conf.py
│   ├── index.rst
│   ├── quickstart.rst
│   ├── api.rst
│   └── development.rst
├── Dockerfile                    # Docker configuration
├── .dockerignore
├── pyproject.toml               # Project configuration
└── README.md
```

## Development

### Using Hatch

Hatch is used for managing the development environment:

```bash
# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Lint code
hatch run lint:check

# Format code
hatch run lint:fmt

# Build documentation
hatch run docs:build

# Serve documentation locally
hatch run docs:serve
```

### Manual Setup (without Hatch)

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=houseelf --cov-report=term-missing

# Lint code
ruff check src tests

# Format code
ruff format src tests
```

## Documentation

Build and view the full documentation:

```bash
# Build the docs
hatch run docs:build

# Serve locally at http://localhost:8000
hatch run docs:serve
```

Or manually:

```bash
pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html
python -m http.server -d docs/_build/html 8000
```

## Deployment to EC2

### Option 1: Using Docker

1. Build and push your Docker image to ECR or Docker Hub:

```bash
# Tag your image
docker tag houseelf:latest your-registry/houseelf:latest

# Push to registry
docker push your-registry/houseelf:latest
```

2. On your EC2 instance, schedule with cron:

```bash
# Edit crontab
crontab -e

# Add entry (example: run daily at 2 AM)
0 2 * * * docker run --rm your-registry/houseelf:latest python -m houseelf.scripts.my_task
```

### Option 2: Using AWS EventBridge

1. Create an ECS task definition with your Docker image
2. Create an EventBridge rule with your desired schedule
3. Set the ECS task as the target

### Option 3: Direct Installation on EC2

```bash
# On EC2 instance
git clone https://github.com/TheWinterShadow/HouseElf.git
cd HouseElf
pip install -e .

# Add to crontab
crontab -e
0 2 * * * cd /path/to/HouseElf && python -m houseelf.scripts.my_task >> /var/log/houseelf.log 2>&1
```

## Environment Variables

Scripts can access environment variables:

```bash
# Run with environment variables
export MY_API_KEY="secret"
python -m houseelf.scripts.my_task

# With Docker
docker run --rm -e MY_API_KEY="secret" houseelf:latest python -m houseelf.scripts.my_task
```

## Logging

All scripts automatically log to stdout with the following format:

```
2025-01-XX HH:MM:SS - ScriptName - INFO - Message
```

Logs can be captured by:
- Docker logs: `docker logs <container_id>`
- CloudWatch Logs (when using ECS)
- File redirection: `python -m script >> logfile.log 2>&1`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or contributions, please open an issue on [GitHub](https://github.com/TheWinterShadow/HouseElf/issues).
