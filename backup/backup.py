
# %%

import subprocess
import datetime
import os
import sys
import io # Still import io, though not directly used for TextIOWrapper in this fix

# %%

# Define your source and destination directories
source_dir = r"U:\VISION\backup\test_transfer"
destination_dir = r"L:\P087\test"

# %%

# Get current date for log file
log_date = datetime.datetime.now().strftime("%Y-%m-%d")
log_file_path = fr"U:\VISION\backup\log_backup_{log_date}.txt"

# Ensure the log directory exists
log_dir = os.path.dirname(log_file_path)
os.makedirs(log_dir, exist_ok=True)

# %%

# Robocopy command and arguments
robocopy_command = [
                    "robocopy",
                    source_dir,
                    destination_dir,
                    "/E",          # Copy subdirectories, including empty ones
                    "/Z",          # Restartable mode
                    "/MT:8",       # Multi-threaded copy (8 threads)
                    "/R:5",        # Retry 5 times on failed copies
                    "/W:10",       # Wait 10 seconds between retries
                    "/ETA",        # Show estimated time of arrival
]

# the /tee argument was implemented in pre/copilot.py : does not make any change on how the percentages are shown.

# %%

print(f"Executing command: {' '.join(robocopy_command)}")
print("\n--- Robocopy Progress (Live) ---")

try:
    # Use subprocess.Popen to run robocopy and capture its stdout/stderr
        # otherwise, the percentage progress would not show up !
    # Set the encoding explicitly for the Popen process itself
        # otherwise you will encounter error probaby because of German letters !
    process = subprocess.Popen(
                                robocopy_command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='cp850', # This decodes bytes to text (str)
                                bufsize=1 # Line-buffered output
    )

    # Open the log file for appending (or 'w' for overwriting)
    with open(log_file_path, 'a', encoding='cp850') as log_file:
        # Read directly from process.stdout, as it's already a text stream
        # This replaces the 'with io.TextIOWrapper(...)' block
        while True:
            line = process.stdout.readline() # line is already a str
            if not line:
                break

            # Write to console
            sys.stdout.write(line)
            sys.stdout.flush() # Crucial for real-time overwriting

            # Write to log file
            log_file.write(line)

        # Capture and print any stderr output (errors)
        stderr_output = process.stderr.read() # stderr_output is already a str
        if stderr_output:
            sys.stderr.write(stderr_output)
            sys.stderr.flush()  # this was meant to flush the output & rewrite it, but doesn't work !
            log_file.write(stderr_output)

    # Wait for the robocopy process to complete and get its exit code
    return_code = process.wait()

    # Check robocopy's exit code
    if return_code <= 7:
        print(f"\nRobocopy completed successfully or with minor issues (Exit Code: {return_code}).")
    else:
        print(f"\nRobocopy encountered an error (Exit Code: {return_code}).")

except FileNotFoundError:
    print(f"Error: The 'robocopy' command was not found. Make sure it's in your system's PATH.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"\nLog file written to: {log_file_path}")

# %%



