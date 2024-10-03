import os
from git import Repo
import logging
from datetime import datetime

# Set up logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# Path to repo directory
REPOS_DIR = os.path.expanduser('~/Desktop/repos')

def push_repos(repo_path):
    try:
        repo = Repo(repo_path)
        # Check if the repo has a remote set up and the repo has uncommitted changes
        if repo.remotes and repo.is_dirty():
            # Add all changes, commit and push
            repo.git.add(A=True)
            repo.index.commit(f"Auto-commit on {datetime.now().strftime(f'%a %b-%d-%y %H:%M %p')}")
            repo.remotes.origin.push()
            log.info(f'Successfully pushed {repo_path}')
        else:
            log.info(f'No remote found for {repo_path}')
    except Exception as e:
        log.error(f'Failed to push {repo_path}: {e}')

def find_and_push_repos(root_dir):
    for dirpath, __, _ in os.walk(root_dir):
    # Check if the current directory is a Git repo
        if os.path.exists(os.path.join(dirpath, '.git')):
            log.info(f'Pushing repo: {dirpath}')
            push_repos(dirpath)

if __name__ == "__main__":
    find_and_push_repos(REPOS_DIR)
