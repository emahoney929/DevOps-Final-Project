# DevOps-Final-Project
Final project for CS491 - DevOps

# Project Overview
This codebase is for a baseball player batting statistics program. Using Beautiful Soup for webscraping,
this program prompts users to pick a baseball player and a year in order to receive stats about the player
during the specified year from the webscraper. The information comes from the website:
https://www.baseball-reference.com/

# Pipeline Overview
After every push is made to the main branch, a workflow is created to in order to conduct unit and integration
tests on the newly pushed code. If the tests are passed, a second workflow is triggered in order to deploy
an updated image of the program to DockerHub.

# CI/CD and Deployment Tools
- GitHub/Git: Used for version control of the codebase.

- Unittest: Python module used for unit and integration testing purposes.

- GitHub Actions: Used for building/testing the program after every push made to the main branch.
  Additonally, if building and testing passes, a workflow is created to deploy to Docker.
  
- Docker: Used for deployment of the project onto DockerHub tagged as the "latest-release."
