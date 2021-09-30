## Solution
This solution2.md4 video illustrates that the solution was comprised of 2 simple changes:
1. Creating post-create.sh bash script file in the .devcontainer folder that contains the code to install the dependencies
```bash 
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev_requirements.txt
```

2. Updating the devcontainer.json file to call the post-create.sh bash script from the postCreateCommand, wired up in the devcontainer.json file
```json
	"postCreateCommand": "/bin/bash -c .devcontainer/post-create.sh",
```

**Make sure that the postCreateCommand along with the other commands are wired up at the bottom of the devcontainer.json file**

## From the Field
### Tip 1
We have standardized bash script file names for onCreateCommand, postCreateCommand and postStartCommand and wire up calls to all 3 regardless if we have any logic in them.  The file names are:
- on-create.sh
- post-create.sh
- post-start.sh

We wire them up as follows:
```json
	// Use 'onCreateCommand' to run commands as part of container creation.
	"onCreateCommand": "/bin/bash -c .devcontainer/on-create.sh",

	// Use 'postCreateCommand' to run commands after the container is created.
	"postCreateCommand": "/bin/bash -c .devcontainer/post-create.sh",

	// Use 'postStartCommand' to run commands every time the container starts.
	"postStartCommand": "/bin/bash -c .devcontainer/post-start.sh"
```

### Tip 2
When making changes to the development container configuration, the first step we take is to test it and validate the change in postCreateCommand.  Once that change is tested, we take the second step which we will illustrate in the next challenge.