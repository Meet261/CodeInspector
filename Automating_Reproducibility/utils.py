# utils.py
import os
import time

# Base directory for all operations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create necessary directories
LOGS_DIR = os.path.join(BASE_DIR, "logs")
REPOS_DIR = os.path.join(BASE_DIR, "repos")
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPOS_DIR, exist_ok=True)

def log_message(project_id, stage, message, execution_log=False):
    """Log a message with timestamp to console and file."""
    # Generate timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the full log message
    log_entry = f"[{timestamp}] [{project_id}] [{stage}] {message}"
    
    # Print to console for non-execution logs
    if not execution_log:
        print(log_entry)
    
    # Write to file (both regular and execution logs)
    log_file = os.path.join(LOGS_DIR, f"{project_id}{'_execution' if execution_log else ''}.log")
    with open(log_file, "a") as f:
        f.write(log_entry + "\n")
