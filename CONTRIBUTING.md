# CONTRIBUTING

Contributing to Cligon is easy.
Cligon is written in Python3 and requires a copy of it on your machine.
Please use Python 3.8.2 or higher.

## Prerequisite

If pip is not installed, install pip by running:

```bash
sudo apt install python3-pip
```

pip is the standard package-management system used to install and manage software packages written in Python.

## Use Virtualenv
Create a virtual env by using:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Packages

```bash
pip install -r requirements.txt
```

## Format & Linting
Additionally, please use Visual Studio Code to ensure proper settings.
This project uses Python Black for formatting and Flake8 for linting and is automatically configured to run on save.

To format all files at once, use: `black .` in your terminal.

To lint files use: `flake8 .` in your terminal.

Ensure you are inside your virtual env (.venv) when using the above commands.

Once these items are installed, you can simply edit any file to your desire.
If you have added a new feature or fixed a bug, please feel free to open a PR.

## Git pre-commit hooks
It is recommended to use git pre-commit hooks for this project.
Please install pre-commit: `pip install pre-commit`
And execute: `pre-commit install` to install git hooks in to the `.git/` directory.