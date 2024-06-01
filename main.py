import os
import subprocess

def run_pbs(folder='pbs'):
    # Check if the folder exists
    if not os.path.exists(folder):
        print(f"Folder '{folder}' does not exist.")
        return
    
    # List all files in the folder
    files = os.listdir(folder)
    
    # Filter files that match the pattern pb1.py, pb2.py, etc.
    pb_files = sorted([f for f in files if f.startswith('pb') and f.endswith('.py')])

    for pb_file in pb_files:
        file_path = os.path.join(folder, pb_file)
        print(f"Running {file_path}...")
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        print(f"Output of {pb_file}:\n{result.stdout}")
        if result.stderr:
            print(f"Error in {pb_file}:\n{result.stderr}")

if __name__ == "__main__":
    run_pbs()
