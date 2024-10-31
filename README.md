![Inspiring Image](https://repository-images.githubusercontent.com/870284572/b9b19342-1938-46cf-9eac-ab31a92682ba)

# DruidicGroveAI
DruidicGroveAI is a research-focused repository dedicated to exploring the latest advancements in deep learning. 
This project serves as a hub for experimenting with state-of-the-art models, algorithms, 
and techniques, aiming to push the boundaries of AI innovation.

# Setup
## Environment Variables
Add the project root directory as `DRUIDIC_GROVE_AI_ROOT_PATH` environment variable.
``` bash
export DRUIDIC_GROVE_AI_ROOT_PATH="/<absolute_path>/DruidicGroveAI"
```

## Setup gcloud CLI
Install `gcloud` on the local machine ([Guide](https://cloud.google.com/sdk/docs/install)).

Authenticate locally to GCP:
```bash
gcloud auth login
```

Set the project ID.
```bash
# List all the projects
gcloud projects list

# Set the project
gcloud config set project <project_id>
```

Create authentication keys.
```bash
gcloud auth application-default login
```

## Justfile
> `just` is a handy way to save and run project-specific commands
> 
> The main benefit it to keep all configuration and scripts in one place.
> 
> It uses the `.env` file for ingesting variables.

You can install it by following the [Documentation](https://just.systems/man/en/chapter_4.html).
Afterward, you can execute existing commands located in the `justfile`.

Type `just` to list all available commands.


## Poetry

> Python packaging and dependency management made easy

### Installation

[Reference Documentation](https://python-poetry.org/)

Run the following command from the terminal:
``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

For **MacOS** with ZSH add the `.local/bin` to the `PATH` environment variable. Modify the `.zshrc` file with the following command:

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Add Dependency
``` bash
# NOTE: Use '--group dev' to install in the 'dev' dependencies list
poetry add <library_name>

poetry add <library> --group dev

poetry add <libarry> --group <group_name>
```

### Install Dependencies
``` bash
# Install the dependencies listed in pyproject.toml [tool.poetry.dependencies]
poetry install

# Use the option '--without test,docs,dev' if you want to esclude the specified group from install
poetry install --without test,docs,dev
```