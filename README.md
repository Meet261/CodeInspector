# CodeInspector
Task 2.4: Browser-based Reproducibility and Evaluation

# Overview
CodeInspector provides researchers with an accessible, browser-based environment to ensure the reproducibility of statistical analyses. This project is part of a broader initiative aimed at enhancing the reproducibility of research by automating the evaluation of R-based statistical codes and their dependencies.

By leveraging Binder-ready repositories and Docker containers, researchers can execute enriched code directly within the browser, without needing to manually install dependencies. This service is powered by GESIS Notebooks, providing a seamless and efficient platform for reproducibility.

# Project Goals
**Dependency Resolution:** We resolve package dependencies from the R ecosystem and data dependencies, ensuring all requirements are fully specified.
Containerization: The resolved dependencies are integrated into Docker images, enabling browser-based code execution.
Evaluation: Code reproducibility is evaluated by:
Verifying all package and data dependencies are identified.
Checking that analyses are fully executable.
Confirming that the published codes reproduce the original results.
The project follows the FAIR principles (Findable, Accessible, Interoperable, Reusable), facilitating researchers' ability to investigate statistical analysis codes efficiently.

# Code Files and Dependencies
Each code file is paired with a Binder container, which includes:

**environment.yml:** Specifies the environment dependencies, ensuring reproducibility of the code.
postBuild: A script for downloading datasets and additional dependencies.
Data files: Automatically downloaded and linked during the setup process.
These containers allow the original code to be run without modification, ensuring faithful replication of the analysis.

### Code Reproducibility Tracker
| **File Name**              | **Dependencies**                                                                                  | **Reproducibility Status** | **Issue/Obstacle**                                                                                                                                                                                        | **Suggested Solution**                                                                                                                                          |
|----------------------------|--------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Git Repository : https://github.com/Meet261/social_status_life_satisfaction `Filename: stadyl_analyses.R`         | `haven`, `psych`, `dplyr`, `car`, `ggplot2`, `interactions`, `lm.beta`, `reghelper`, `Hmisc`     | Not Reproducible            | The dataset is read from a local path (`/Users/maria/Documents/projects/_collabs/anticip_status/data/StadyL_Study2.sav`). This path is specific to a local machine and not accessible in Binder.             | Upload the dataset to a public repository (e.g., OSF) and download it during the Binder setup using a `postBuild` file with the `wget` command.                 |


