Development Guide
=================

Setting Up Development Environment
-----------------------------------

1. Clone the repository:

.. code-block:: bash

    git clone https://github.com/TheWinterShadow/HouseElf.git
    cd HouseElf

2. Install development dependencies using hatch:

.. code-block:: bash

    pip install hatch

3. Run tests:

.. code-block:: bash

    hatch run test

4. Run linting:

.. code-block:: bash

    hatch run lint:check

5. Format code:

.. code-block:: bash

    hatch run lint:fmt

Project Structure
-----------------

.. code-block:: text

    HouseElf/
    ├── src/
    │   └── houseelf/
    │       ├── __init__.py
    │       ├── base_script.py
    │       └── scripts/
    │           ├── __init__.py
    │           └── example_script.py
    ├── tests/
    │   └── (test files)
    ├── docs/
    │   ├── conf.py
    │   ├── index.rst
    │   ├── quickstart.rst
    │   ├── api.rst
    │   └── development.rst
    ├── Dockerfile
    ├── .dockerignore
    ├── pyproject.toml
    └── README.md

Running Tests
-------------

Run all tests:

.. code-block:: bash

    hatch run test

Run tests with coverage:

.. code-block:: bash

    hatch run test-cov

Building Documentation
----------------------

Build the HTML documentation:

.. code-block:: bash

    hatch run docs:build

Serve the documentation locally:

.. code-block:: bash

    hatch run docs:serve

Then visit http://localhost:8000 in your browser.

Adding New Scripts
------------------

1. Create a new file in ``src/houseelf/scripts/``
2. Inherit from ``BaseScript``
3. Implement the ``run()`` method
4. Add a ``main()`` function for CLI execution
5. Document your script using docstrings
6. Add tests in ``tests/``

Code Style Guidelines
---------------------

* Follow PEP 8 style guidelines
* Use type hints where appropriate
* Write comprehensive docstrings
* Keep functions small and focused
* Add tests for new functionality

Continuous Integration
----------------------

The project uses GitHub Actions for CI/CD (to be configured):

* Code formatting with black and isort
* Linting with flake8
* Type checking with mypy
* Testing with pytest
* Documentation building with Sphinx
* Docker image building
