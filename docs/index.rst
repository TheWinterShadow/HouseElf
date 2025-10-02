Welcome to HouseElf's documentation!
====================================

HouseElf is a Python package for running daily automation tasks periodically 
in Docker containers on EC2 instances. It provides a simple framework for 
creating, managing, and executing scheduled tasks that log their output and 
exit cleanly.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   api
   development

Features
--------

* Simple base class for creating automation scripts
* Built-in logging with consistent formatting
* Error handling and exit code management
* Docker support for containerized execution
* Easy integration with scheduling systems (cron, AWS EventBridge, etc.)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
