# Moving the customizations from postCreateCommand to the local Dockerfile
Once we have validated the code in the bash script, the next step is to move the changes to the local Dockerfile.  This brings us back to the tip from solution1:

## (from solution 1) From the Field 
We never just have an image pointer in devcontainer.json like below:
```json
{
    "image": "python:3.9"
}
```

Even if we are just using the base image, we have a Dockerfile with a FROM and point to the image.  Below is a simplified equivelant to the above, using a Dockerfile:
```json
{
	"build": {
		"dockerfile": "Dockerfile"
	}
}
```

```Dockerfile
FROM python:3.9
```

This refactor illustrates why that tip is in place.  We already have a Dockerfile in our solution where we can move our changes.

## Challenge
Move the logic that installs the dependencies for the application from the bash script file to the local Dockerfile.
