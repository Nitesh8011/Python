import subprocess

def list_directory_contents():
    try:
        # Run the 'ls' command
        result = subprocess.run(['ls', '-l'], check=True, text=True, capture_output=True)
        
        # Print the standard output
        print("Directory contents:\n", result.stdout)

    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to list the directory contents.")
        print("Return code:", e.returncode)
        print("Error message:", e.stderr)

if __name__ == "__main__":
    list_directory_contents()