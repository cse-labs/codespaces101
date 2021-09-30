## Solution
.devcontainer in this branch has the devcontainer.json and Dockerfile created from the predefined configurations.

The video Solution1.mp4 shows the following:
- Creating the configuration
- Opening the develpoment container 
- Installing the prerequisites
- Running the tests with pytest

## From the Field
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

The reason we have standardized on this approach is that our approach to developing development containers ends up with tested solutions encapsulated in our Docker image.  However, prior to baking changes directly into the image (stored in a registry), we walk through 2 other stages.  We will explore those in the upcoming challenges.