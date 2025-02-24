import subprocess

def clone_repo(repo_url, destination_dir):
    try:
        # Run the git clone command
        subprocess.run(["git", "clone", repo_url, destination_dir], check=True)
        print(f"Repository cloned successfully into {destination_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")

# Specify the repository URL and the destination directory
repo_url = "https://github.com/udacity/dsnd-dashboard-project.git"
destination_dir = "path/to/your/project/folder"

# Call the function to clone the repository
#clone_repo(repo_url, destination_dir)

