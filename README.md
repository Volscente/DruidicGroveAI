# ds-repository-template

# Introduction
The repository includes the code for providing utils modules and functions.

# Installation
- Ensure to have `gcloud` installed
- Ensure to have the latest version of Poetry installed
```bash
poetry self update
```
- Setup the authentication to the Artifact Repository following [this guide](https://cloud.google.com/artifact-registry/docs/python/authentication?_ga=2.246859213.-858896186.1676536949#before_you_begin)
  - Install the following libraries
  ```bash
  poetry add twine keyring keyrings.google-artifactregistry-auth
  ```
  - Run the following command
  ```bash
  gcloud artifacts print-settings python --project=PROJECT \
    --repository=REPOSITORY \
    --location=LOCATION
  ```
  - Copy the output to the respective files (`$HOME/.pypirc` and `./venv/pip.conf`)
    - The `./venv/pip.conf` might be in the repository folder or in the `$HOME/Library/Caches/pypoetry/virtualenvs/<name_of_the_venv`)
  - Login into `gcloud`
  ```bash
  gcloud auth login
  ```
- Add the Artifact Repository as a source to the `pyproject.toml`
```bash
poetry source add --priority=supplemental <choose_name_for_the_source> https://<LOCATION>-python.pkg.dev><PROJECT_ID>/<ARTIFACT_REPOSITORY_NAME>/simple

# Example
poetry source add --priority=supplemental vg-ds-utils-artifact-repository-source https://europe-west3-python.pkg.dev/dh-vp-stg-7026/vg-ds-utils-artifact-repository/simple/
```
**NOTE:** Sometimes the addition of the `/simple` might fix the impossibility of finding the remote source
- Add the Python Package to the dependencies
```bash
poetry add --source <name_of_the_choosen_source> <package_name_to_install>

# Example
poetry add --source vg-ds-utils-artifact-repository-source vg-ds-utils
```

# Setup

## Update PYTHONPATH
Add the current directory to the `PYTHONPATH` environment variables.
``` bash
export PYTHONPATH="$PYTHONPATH:/<absolute_path>/<parent_folder>"
```

## Install gcloud CLI
Follow this [documentation](https://cloud.google.com/sdk/docs/install-sdk) to install the gcloud CLI.

**NOTE:** Ensure to run the `gcloud init` command to initialise the CLI.

## Poetry

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

### Init Repository
```bash
poetry init
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

