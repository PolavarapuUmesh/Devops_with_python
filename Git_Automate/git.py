'''This script will automate the task of pulling the latest code from a Git repository, building and running a Docker container, creating a file inside the container, and finally committing and pushing changes back to the Git repository'''
import subprocess

def automate_task():
    try:
        subprocess.run(['git', 'pull', 'origin', 'main'], check=True)
        
        # Build the Docker image
        subprocess.run(['docker', 'build', '-t', 'my_image', '.'], check=True)
        
        # Run the Docker container
        subprocess.run(['docker', 'run', '-d', '--name', 'my_container', '-p', '8080:8080', 'my_image'], check=True)
        
        # Execute commands inside the running container
        subprocess.run(['docker', 'exec', '-it', 'my_container', 'bash', '-c', 
                        'mkdir /app/new_dir && touch /app/new_dir/newfile.txt && echo "Hello, World!" > /app/new_dir/newfile.txt'], check=True)
        
        # Check the file created inside the container
        subprocess.run(['docker', 'exec', '-it', 'my_container', 'cat', '/app/new_dir/newfile.txt'], check=True)
        
        # Commit changes to the Git repository
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Automated commit from script'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)

        # Tag the new version
        subprocess.run(['git', 'tag', '-a', 'v1.0', '-m', 'Released version 1.0'], check=True)
        subprocess.run(['git', 'push', 'origin', '--tags'], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return

def main():
    automate_task()

if __name__ == "__main__":
    main()
    # subprocess.run(['docker', 'stop', 'my_container'], check=True)
    # subprocess.run(['docker', 'rm', 'my_container'], check=True)
    # subprocess.run(['docker', 'image', 'rm', 'my_image'], check=True)
    # subprocess.run(['docker', 'system', 'prune', '-f'], check=True)
    # subprocess.run(['docker', 'volume', 'prune', '-f'], check=True)
    # subprocess.run(['docker', 'composer', 'up', '-d'], check=True)
    # subprocess.run(['docker', 'composer', 'down'], check=True)
    # subprocess.run(['docker', 'volume', 'create', 'my-volume'], check=True)
    # subprocess.run(['docker', 'composer', 'up', '-d'], check=True)
    # subprocess.run(['docker', 'container', 'ls', '-a'], check=True)
    # subprocess.run(['docker', 'container', 'stop', 'my_container'], check=True)
    # subprocess.run(['docker', 'container', 'rm', 'my_container'], check=True)
    # subprocess.run(['docker', 'image', 'ls'], check=True)
    # subprocess.run(['docker', 'image', 'rm', 'my_image'], check=True)
    # subprocess.run(['docker', 'image', 'prune', '-f'], check=True)
    # subprocess.run(['docker', 'network', 'ls'], check=True)
    # subprocess.run(['docker', 'network', 'prune', '-f'], check=True)
    # subprocess.run(['docker', 'volume', 'ls'], check=True)
    # subprocess.run(['docker', 'volume', 'prune', '-f'], check=True)
    # subprocess.run(['docker', 'system', 'prune', '-f'], check=True)
    # subprocess.run(['docker', 'info'], check=True)
    # subprocess.run(['docker', 'version'], check=True)
    # subprocess.run(['docker', 'login'], check=True)
    # subprocess.run(['docker', 'logout'], check=True)
    # subprocess.run(['docker', 'images', '-q'], check=True)
    # subprocess.run(['docker', 'rmi', '$(docker images -f "dangling=true) -q)'], check=True)
    # subprocess.run(['docker', 'rmi', '-f', '$(docker images -q)])
    #                 subprocess.run(['docker', 'rmi', '-f', '$(docker images -q)
    #                 subprocess.run(['docker', 'rmi', '-f', '$(docker images -q)
    #                                 subprocess.run(['docker', 'rmi', '-f', '$(docker images -q',)]
                                                                            
    
    