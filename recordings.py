import subprocess
import time

script = "/usr/local/bin/move_recordings.sh"

while True:
    print(f"Running: {script}")
    result = subprocess.run(["sudo", script], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error:", result.stderr.strip())
    else:
        print("Success:", result.stdout.strip())
    
    time.sleep(1)  # Wait for 1 second
