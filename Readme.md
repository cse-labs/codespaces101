# Table of Contents
I. [Overview](#overview)<br/>
&nbsp;&nbsp;&nbsp;A. [Why you care](#why-you-care)<br/>
&nbsp;&nbsp;&nbsp;B. [What you will learn](#what-you-will-learn)<br/>
II. [How this training is structured](#how-this-training-is-structured)<br/>
III. [Requirements](#requirements)<br/>
IV. [Overview of Development containers, GitHub Codespaces And Visual Studio Code](#overview-of-development-containers-github-codespaces-and-visual-studio-code)<br/>
&nbsp;&nbsp;&nbsp;A. [Development Container](#development-container)<br/>
&nbsp;&nbsp;&nbsp;B. [Visual Studio Code](#visual-studio-code)<br/>
&nbsp;&nbsp;&nbsp;C. [GitHub Codespaces](#github-codespaces)<br/>
V. [Challenges](#challenges)<br/>
&nbsp;&nbsp;&nbsp;A. [Challenge1](Challenges/Challenge1.md)<br/>
&nbsp;&nbsp;&nbsp;B. [Challenge2](Challenges/Challenge2.md)<br/>
&nbsp;&nbsp;&nbsp;C. [Challenge3](Challenges/Challenge3.md)<br/>
&nbsp;&nbsp;&nbsp;D. [Challenge4](Challenges/Challenge4.md)<br/>
&nbsp;&nbsp;&nbsp;E. [Challenge5](Challenges/Challenge5.md)<br/>
&nbsp;&nbsp;&nbsp;E. [Challenge6](Challenges/Challenge6.md)<br/>

# Overview
## Why you care
Traditionally, there is considerable friction for developers when setting up development environments.  It is not uncommon for devs new to projects to spend days updating their environment before being able to start contributing to the project.  

The more complex the requirements, the greater the friction.  Consider the following 2 examples:
1. Configuring a local Kubernetes development environment with the following:
- Grafana
- Prometheus
- Fluentbit
2. A Python API with:
- The current version of Python
- Debugging configured
- Pytest
- Flask

The above are 2 very real examples.  The Retail Dev Crew team in CSE has been working with some of the largest Kubernetes deployments in the world.  The dev environment includes everything listed above in example #1 plus much more.  Despite the complex dev environment, the team prides itself upon new devs creating a PR on their first day.  This is only possible because the Retail Dev Crew's use of development containers and GitHub Codespaces.  

Python environments are notoriously challenging to configure.  This is especially true with regard to debugging.

A large blocker to contributing to OSS projects is configuring the development environment.  Imagine being able to instantiate a fully-configured development environment with the click of a button.  That is the promise of development containers and GitHub Codespaces.

## What you will learn
If you complete this self-directed training, you will:
- Learn what development containers are
- Learn what GitHub Codespaces are
- Understand the relationship between Visual Studio Code, development containers and GitHub Codespaces
- Learn how to build devcontainers
  - Using an existing docker image
  - Using the commands 
    - onCreateCommand
    - postCreateCommand
    - postStartCommand
  - Creating a custom docker image
  - Updating the developer experience
    - Installing extensions
    - dotfiles
- Patterns and best practices working with development containers and GitHub Codespaces

# How this training is structured
This GitHub repository has a master branch and a collection of solution branches.

The master branch contains the following:
- Readme.md - The main training file.  Start here.
- Challenges/* - The challenge files for this training.  Each Challenge file will contain some learnings/background on the challenge, the challenge itself and, optionally, some helpful hints.
- api/math_api.py - A very simple python Flask REST API
- tests/api/test_math_api.py - Pytest unit tests
- requirements.txt and dev_requirements.txt - Python requirements files containing the dependencies for the application and application development environment
- math.http - A manual test file for use in Challenge 5

Each challenge has its own solution branch.  Use your git client to open each Solution branch.  For example:
```bash
git checkout Solution1

# Or if you don't have the solution branch local
git checkout --track origin/Solution1
```

Each branch contains the following:
- Solution(1-N).md - File describing the solution.  **This file may also contain a "From the Field" section where we list some of the learnings the CSE Retail Dev Crews team has had working with GitHub codespaces with our largest customers**
- The solution configured in the .devcontainer folder
- Solution(1-N).mp4 - A video outlining a solution to the challenge.  **Open the videos from the file system, not Visual Studio Code**


# Requirements
You will need the following to complete the development container challenges in this training [(see detailed installation instructions here)](https://code.visualstudio.com/docs/remote/containers#_system-requirements):
- Docker for Windows/Mac/Linux
- Visual Studio Code

You will need to be enabled for GitHub Codespaces in order to complete the codespaces challenges.  [(see documentation here about getting access to Codespaces)](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/enabling-codespaces-for-your-organization)



# Overview of Development containers, GitHub Codespaces And Visual Studio Code
The goal of these technologies is to allow developers to define a fully-configured development environment, run it in a container and develop against it with Visual Studio Code running as a client application or running in the browser.  This section will provide a high-level overview of these technologies and how they interrelate.  You will find links to more information throughout this section.

## Development Container
As noted above, a development container is a fully-featured development environment running in a container.  The development container is a Docker container running locally or remotely that, at a high-level, contains the following:
- All the application dependencies - Defined in a Docker image, Dockerfile or docker-compose file and potentially updated via scripts called by well-defined hooks.
- The application code - mounted, copied or cloned into the container
- Visual Studio Code Server - configured with the appropriate Visual Studio Code Extensions required to develop

[Default Images](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#using-the-default-configuration) can be used for general development.  However, for a more productive development experience, you will likely want to define your own development containers.  The configuration for the development container is in a [devcontainer.json](https://code.visualstudio.com/docs/remote/devcontainerjson-reference) file which exists either at the root of the project or under a .devcontainer folder at the root.  **From the field: We always put the devcontainer.json file under a .devcontainer folder.  We do that because we always have additional files that accompany the devcontainer.json file.  These files include bash scripts and a Dockerfile.  We will get into more details about these files later.**  During the challenges in this training you will explore and learn the common configuration patterns in a devcontainer.json file.  For the time being, we will show you a [very simple example of a devcontainer.json file](https://code.visualstudio.com/docs/remote/containers#_create-a-devcontainerjson-file) taken from the documentation:

```json
{
  "image": "mcr.microsoft.com/vscode/devcontainers/typescript-node:0-12",
  "forwardPorts": [3000],
  "extensions": ["dbaeumer.vscode-eslint"]
}
```
Again, we will explore each of the above in more detail in the challenges.  For now, it is enough to understand that the devcontainer.json points to an existing typescript-node image.  This is the image that will be used when starting the developer (Docker) container.  The configuration further specifies that port 3000 should be forwarded from the container to the host.  Lastly, it specifies that a linting extension should be installed in the VS Code Server running in the developer container.

## Visual Studio Code
Visual Studio Code has a [Remote-Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) that enables the use of a Docker container as a fully configured development environment.  This is enabled through a client-server architecture.  As noted above, running development containers have a Visual Studio Code Server running in them.  The Visual Studio Code Client can access a running container or can create an instance of a new development container and connect to it.

The challenges will mainly be using Visual Studio Code to create and run development containers.

## GitHub Codespaces
GitHub Codespaces enables exposing a fully configured development environment for GitHub repositories.  This can be used for anthing from new feature development to code reviews.  Codespaces extends the use of development containers by providing a remote hosting environment for them.  Developers can simply click on a button in GitHub to open a Codespace for the repo.  Behind the scenes, GitHub Codespaces is:
- Spinning up a VM
- Shallow cloning the repo in that VM.  The shallow clone pulls the devcontainer.json onto the VM
- Spins up the development container on the VM 
- Clones the repository in the development container
- Connects you to the remotely hosted development container - via the browser or GitHub

# The Challenges - Building a Devcontainer
The challenges below are designed to provide a stepwise approach to building development containers.  They start with the simplist approach, with each subsequent challenge teaching you a further aspect.  Throughout the challeges, we will be providing real-world guidance that we have learned working with real customers in the field.
- [Challenge1](Challenges/Challenge1.md)
- [Challenge2](Challenges/Challenge2.md)
- [Challenge3](Challenges/Challenge3.md)
- [Challenge4](Challenges/Challenge4.md)
- [Challenge5](Challenges/Challenge5.md)
- [Challenge6](Challenges/Challenge6.md)

