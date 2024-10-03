# Auto Git Push Script

## Description

This Python script automatically pushes all changes in your local Git repositories to their corresponding GitHub repositories. It can traverse through multiple directories, detect if a folder is connected to a Git repository, and push changes automatically. You can schedule this script to run at a specified time, such as midnight, using a cron job (or a scheduling tool on macOS).

## Features
  * Automatically pushes all changes in your Git repositories to GitHub.
  * Traverses subdirectories to detect and push changes in nested repositories.
  * Logs actions, including successes and failures, for easy tracking.
  * Supports virtual environments and is easy to configure.
  * Customizable through environment variables or command-line parameters.

## Prerequisites
Make sure the following dependencies are installed:
* Git: The script relies on Git to push changes. You can install it with Homebrew:
  ```bash
   brew install git
  ```
* Python 3.8+: Ensure Python is installed. You can check the version by running:
  ```bash
  python3 --version
  ```

* GitPython library: This script uses the `GitPython` library to interact with repositories. Install it in your virtual environment:
  ```bash
   pip install gitpython
  ```

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/EricDavenport/auto-git-script.git
    cd auto-git-script
    ```
1. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

1. Add your repositories: You can organize your repositories in a folder of your choice. The script will check all subdirectories.
1. Configure the script:
   * By default, the script searches the `repos/` directory. Update the script to point to the directory where you keep your repositories if it differs from the default.

## Usage
1. Run the script manually:
    To run the script manually and push your repositories, execute:
    ```bash
    python push_repos.py
    ```

1. Schedule it with cron (optional):
    To run this script automatically at midnight every day, add the following cron job (on macOS):
    ```bash
    crontab -e
    ```
    Add the following line to schedule the script at midnight:

    ```bash
    0 0 * * * /path/to/your/virtualenv/bin/python /path/to/auto-git-script/push_repos.py
    ```
    Make sure you replace /`path/to/your/virtualenv/bin/python` and `/path/to/auto-git-script/push_repos.py` with the actual paths.

## Logging

The script generates a log file (`logfile.log`) that keeps track of:
* Repositories successfully pushed.
* Any errors encountered during the push process.

You can check this log for details on the script's execution.

## .gitignore

Make sure to add sensitive or unnecessary files (e.g., virtual environments, logs) to your `.gitignore`. Here's a sample:
```bash

# Virtual environment
venv/

# Logs
logfile.log

# Byte-compiled / optimized files
__pycache__/
*.py[cod]

# System files
.DS_Store
```

## Troubleshooting
* Error: No module named `git`: Ensure that the `GitPython` module is installed by running `pip install gitpython`. Verify that the correct Python environment is being used (`which python` should point to the virtual environment’s Python).
Permission issues: If you face permission issues when running the script via cron, ensure the paths in your cron job are correct and accessible.

## Contributing
If you have suggestions for improvements or encounter any bugs, feel free to open an issue or submit a pull request.
