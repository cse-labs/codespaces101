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

## From the Field
Moving changes from the postCreateCommand to the Dockerfile under .devcontainer is the second step in a 3-step process we follow when developing our dev containers.  Once this change has been validated, the third step is to move that change to our base images we maintain in a separate pipeline and store in a container registry.

We maintain a separate pipeline for our base docker images for several reasons, including:
- We can have pipelines trigger to keep the images up to date
- We can do security scanning
- We can test the images