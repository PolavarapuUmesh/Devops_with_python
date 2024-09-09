# import os
# import subprocess

# def git_operation(repo_dir, commit_message):
#     try:
#         os.chdir(repo_dir)
#         subprocess.run(['git', 'pull'], check=True)
#         subprocess.run(['git', 'add', '.'], check=True)
#         subprocess.run(['git', 'commit', '-m', commit_message], check=True)
#         subprocess.run(['git', 'push'], check=True)
#         print("Git operations completed successfully.")
#     except Exception as e:
#         print(f"Error during Git operations: {e}")
# repo_dir = '/home/umesh/Desktop/Devops_with_python/Devops_with_python'
# commit_message = 'Automated commit message'
# git_operation(repo_dir, commit_message)


# import os
# import subprocess

# def git_operation(repo_dir, commit_message):
#     try:
#         os.chdir(repo_dir)
#         subprocess.run(['git', 'pull'], check=True)
#         subprocess.run(['git', 'add', '.'], check=True)
#         result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
#         if result.stdout:
#             subprocess.run(['git', 'commit', '-m', commit_message], check=True)
#             subprocess.run(['git', 'push'], check=True)
#             print("Git operations completed successfully.")
#         else:
#             print("No changes to commit.")
            
#     except subprocess.CalledProcessError as e:
#         print(f"Git command failed with exit code {e.returncode}.")
#         print(f"Command: {' '.join(e.cmd)}")
#         print(f"Error Output: {e.output.decode('utf-8') if e.output else 'No output'}")
#     except Exception as e:
#         print(f"Error during Git operations: {e}")

# repo_dir = '/home/umesh/Desktop/Devops_with_python/Devops_with_python'
# commit_message = 'Automated commit message'

# git_operation(repo_dir, commit_message)

import os
import subprocess

def git_add_all():
    """
    Adds all changes to the staging area.
    """
    subprocess.run(["git", "add", "."])

def git_commit(message):
    """
    Commits all changes with the given message.
    """
    subprocess.run(["git", "commit", "-m", message])

def git_push():
    """
    Pushes all changes to the remote repository.
    """
    subprocess.run(["git", "push"])

def main():
    """
    Performs the Git operations: add, commit, push.
    """
    git_add_all()
    git_commit("Updated files")
    git_push()

if __name__ == "__main__":
    main()