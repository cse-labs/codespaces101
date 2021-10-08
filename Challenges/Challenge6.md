# GitHub Codespaces
As you read in the Readme.md file, devcontainers provide the ability to define fully-configured development environments.  GitHub Codespaces builds upon devcontainers to allow for a one-click hosted development environment.  The following are some of the key benefits of GitHub Codespaces:
- The only prerequisite is a modern browser.  While devcontainers have minimal prerequisites, they do require Docker and Visual Studio Code to be installed.
- Codespaces allows developers to add features, fix bugs or review PRs without installing anything on their machine.

This challenge will illustrate the power of GitHub Codespaces.

# Challenge
- Open the repository in GitHub Codespaces
- Perform the following using the browser client
  - Run the API in debug mode
  - Set a breakpoint on line 10 in api/math_api.py
  - Click on 'Send Request' in math.http just above
    ```bash
    GET http://localhost:5000/add?x=100&y=10101 HTTP/1.1
    ```
  - Debug through the call to add
- Perform the same steps above using Visual Studio Code as the client 

# Helpful Hints
- You have several choices with regard to the repository and branch you open in GitHub Codespaces:
  - You can use the Solution5 or Solution6 branch in https://github.com/RobBagby/codespaces-training
  - You can use fork  https://github.com/RobBagby/codespaces-training and push to your own GitHub repository and
    - Use the Solution5 or Solution6 branch
    - Use master, as long as you have followed all the challenges
- You have to have access to GitHub CodeSpaces in order to follow this challenge 