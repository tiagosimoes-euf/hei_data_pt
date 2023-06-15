# Python 3.x CLI application starterkit

Boilerplate CLI application with some utilities.

## Installation

Requires Python 3.8+ to run. To start the virtual environment run the following commands:

    python3 -m venv venv
    source venv/bin/activate

To install the required dependencies run the following command:

    pip install -r requirements.txt

For development purposes, run the following command instead:

    pip install -r requirements-dev.txt

## Usage

This application can perform several operations, each requiring the execution of a particular command inside the virtual environment mentioned above:

    python starterkit/manage.py <command>

### List of commands

- The `fancydemo` command showcases formatted CLI output used in scripts.
- The `lint` command enforces style guide and sorts imports in scripts.
- The `shell` command provides an interactive Python shell.
