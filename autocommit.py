# autocommit.py

import git
from datetime import datetime

def auto_commit_and_push(repo_path, files_to_commit):
    """
    Automatically stages, commits, and pushes specified files in the repository.

    Parameters:
        repo_path (str): Path to the git repository.
        files_to_commit (list): List of file paths to commit.
    """
    # Ensure index.html is included in the list of files to commit
    if 'index.html' not in files_to_commit:
        files_to_commit.append('index.html')
        
    try:
        repo = git.Repo(repo_path)
        # Ensure files are staged for commit
        repo.index.add(files_to_commit)
        
        # Create a timestamped commit message
        commit_message = f"Automatic update on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        repo.index.commit(commit_message)
        
        # Push to the main branch
        origin = repo.remote(name="origin")
        origin.push()
        
        print("Files committed and pushed successfully.")
    except Exception as e:
        print(f"An error occurred while committing and pushing files: {e}")
