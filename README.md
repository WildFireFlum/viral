# Viral

**Viral** is a command-line interface application built with [Typer](https://typer.tiangolo.com/) ...

## Installation

To run **Viral**, you need to run the following steps:

1. Download the application's source code to a `viral/` directory
2. Create a Python virtual environment and activate it

```sh
$ cd viral/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the dependencies

```sh
(venv) $ python -m pip install -r requirements.txt
```

3. Initialize the application

```sh
(venv) $ python -m viral init
```

This command only initialize an empty config file.

## Usage

Once you've download the source code and run the installation steps, you can run the following command to access the application's usage description:

```sh
$ python -m viral --help
Usage: viral [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --help                Show this message and exit.

Commands:
  init      Initialization.
```

You can also access the help message for specific commands by typing the command and then `--help`.
Calling `--help` on each command provides specific and useful information about how to use the command at hand.

## Features

**Viral** has the following features:

| Command            | Description              |
| ------------------ | ------------------------ |
| `init`             | Initialize config file.  |

## Release History

- 0.1.0
  - A work in progress
