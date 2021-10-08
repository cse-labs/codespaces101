## Solution
This solution3.md4 video illustrates that the solution was comprised of 2 simple changes:
1. Removed the commands in post-create.sh (the file will contain no commands to run)
   You could delete the file altogether and remove the call to it.  However, we discussed in Solution2, we have standardized on having calls to postCreateCommand, postStartCommand and onStartCommand wired up.  To that end, we simply removed the commands in the wired up script file.

2. Update the Dockerfile to install the prerequisites
```Dockerfile
COPY *requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/dev_requirements.txt \
   && rm -rf /tmp/pip-tmp
```

## From the Field 1 - Pattern
Moving changes from the postCreateCommand to the Dockerfile under .devcontainer is the second step in a 3-step process we follow when developing our dev containers.  Once this change has been validated, the third step is to move that change to our base images we maintain in a separate pipeline and store in a container registry.

We maintain a separate pipeline for our base docker images for several reasons, including:
- We can have pipelines trigger to keep the images up to date
- We can do security scanning
- We can test the images
- We can publish the images to a container registry
- This approach saves a dramatic amount of time when starting the devcontainer/codespace

## From the Field 2 - Take advantage of prebuilt images in CSE Labs 
If you are doing docker-in-docker or Kubernetes development, you can take advantage of prebuilt images in [CSE Labs](https://github.com/cse-labs).  
- The [codespaces-images](https://github.com/cse-labs/codespaces-images) are maintained here
- They are published to the following container registry: ghcr.io/cse-labs
- You can take advantage of the CSE Retail DevCrew Image Supply Chain.  The images are:
   - Up to date - The images are updated weekly.  The pipeline uses curl to pull in the latest scripts published by the GitHub codespaces team.
   - Standard
