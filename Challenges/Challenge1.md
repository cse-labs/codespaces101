# Using predefined container configurations
## Background
In order to learn about configuring development containers, it is helpful to start with the simplist definition.  The simplist .devcontainer/devcontainer.json file has only an image entry.  
```json
{
    "image": "python:3.9"
}
```

Although the above works, you will likely want a more helpful configuration.  If you are getting started building a devcontainer, the easiest way is to get started is to use the [predefined container configurations](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#using-a-predefined-container-configuration) that are available.  They provide a good starting development environment configuration for different environments.

## Challenge
In this challenge, you need to accomplish the following, using **Visual Studio Code**:
- Using a predefined container configuration, create a development container configuration
- Open the root folder (Codespaces) in a development container (Remote-Containers)
- Run the python tests.  6 should pass.  In order to run the tests, you need to open a bash terminal in the development container and run the following:
```bash
$ pytest
```
You should see the following (or something like it)
```bash
====================================================== test session starts =======================================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /workspaces/Codespaces
plugins: mock-3.6.1
collected 6 items                                                                                                                

tests/api/test_math_api.py ......                                                                                          [100%]

======================================================= 6 passed in 0.32s ========================================================
```

## Helpful hints
- You will need to clone this repo so you have the code locally
- You can find information about [predefined container configurations here](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#using-a-predefined-container-configuration)
- You will need to have the Remote-Containers extension installed in Visual Studio Code
- You can find the helpful commands in VS Code by pressing (Ctrl+Shift+P on Windows) or (Cmd+Shift+P on a Mac) and typing "Remote-Containers".  You will see the remote containers options in the menu.
- This is a Python app 
  - You can use Python 3.9
  - The requirements.txt file holds all the dependencies required by the application
  - You can install the requirements by running the following in a bash terminal:
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install -r dev_requirements.txt
    ```
- **Important - You will need to choose Remote-Containers: Rebuild Container" if you want to see a change you made and you have already built the remote container.