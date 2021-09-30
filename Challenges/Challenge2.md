# Customizing the development container with the onCreateCommand hook
## Background
You likely noticed in Challenge1 that the default Python development environment configuration did not yield a development environment that was fully configured for the application.  You were forced to further configure the environment for the application dependencies in order to run the tests or access the api.  This is certainly not ideal, as every developer would have to **know** both that they need to install the dependencies **and** how to install them.  A better solution would be to have the dependencies installed in the development environment.
[Development containers](https://code.visualstudio.com/docs/remote/devcontainerjson-reference) have hooks that allow you to run commands at different points in the development container lifecycle.  These include:
- onCreateCommand - Run when creating the container
- postCreateCommend - Run inside the container after it is created
- postStartCommand - Run every time the container starts

## Challenge
In this challenge, you will use the postCreateCommand to install the application dependencies.


## Helpful Hints
- Remember that in challenge 1 you needed to run the following in a bash terminal:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev_requirements.txt
```


"onCreateCommand": "/bin/bash -c .devcontainer/on-create.sh"

## From the Field
