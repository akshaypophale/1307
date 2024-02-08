import subprocess
# Navigate to the repository directory
repo_path = '/path/to/your/repository'
text_file_path = '/path/to/your/text_file.txt'
# Change directory to the repository
os.chdir(repo_path)
# Add the file to the repository
subprocess.run(["git", "add", "."])
# Commit the changes
subprocess.run(["git", "commit", "-m", "text file found"])
# Push the changes to the remote repository
subprocess.run(["git", "push"])