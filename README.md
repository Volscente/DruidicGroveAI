![Inspiring Image](https://repository-images.githubusercontent.com/870284572/b9b19342-1938-46cf-9eac-ab31a92682ba)

# DruidicGroveAI
DruidicGroveAI is a research-focused repository dedicated to exploring the latest advancements in deep learning. 
This project serves as a hub for experimenting with state-of-the-art models, algorithms, 
and techniques, aiming to push the boundaries of AI innovation.

# Resources
The full documentation of the project can be found in the dedicated [GitHub Pages](https://volscente.github.io/DruidicGroveAI/).

For the developers, check the wiki [Package & Modules](https://github.com/Volscente/DruidicGroveAI/wiki/Packages-&-Modules) Section.

Please refer to this [Contributing Guidelines](https://github.com/Volscente/DruidicGroveAI/wiki/Contributing-Guidelines) in order to contribute to the repository.

# Setup
## Environment Variables
Add the project root directory as `DRUIDIC_GROVE_AI_ROOT_PATH` environment variable.
``` bash
export DRUIDIC_GROVE_AI_ROOT_PATH="/<absolute_path>/DruidicGroveAI"
```
Create a `.env` file in the root folder like
```
# Set the Root Path
DRUIDIC_GROVE_AI_ROOT_PATH="/<absolute_path>/DruidicGroveAI"
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

## Pre-commit
```bash
# Install
pre-commit install

# Check locally
pre-commit run --all-files
```