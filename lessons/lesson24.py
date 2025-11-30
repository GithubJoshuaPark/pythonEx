# lessons/lesson24.py
import os
import sys
import subprocess
import utils

utils.show_base_name(__file__, True)

# This lesson demonstrates virtual environments and requirements.txt
# It will guide you through setting up a virtual environment and
# installing/managing dependencies.

def main():
    """
    This lesson guides through creating and using virtual environments
    and managing dependencies with requirements.txt.
    """
    print("--- Lesson 24: Virtual Environments and requirements.txt ---")

    # 1. What is a Virtual Environment?
    # A virtual environment is a self-contained Python environment.
    # It allows you to manage dependencies for different projects separately.
    # This avoids conflicts between package versions required by different projects.

    print("\n--- 1. Understanding Virtual Environments ---")
    print("Imagine having multiple Python projects, each needing different versions of libraries.")
    print("Without virtual environments, installing a new version for one project might break another.")
    print("Virtual environments solve this by creating isolated spaces for each project.")
    print("-" * 20)

    # 2. Creating a Virtual Environment
    # The 'venv' module (built-in since Python 3.3) is used to create them.
    # We'll create one named '.venv' in the project root.

    print("\n--- 2. Creating a Virtual Environment (.venv) ---")
    print("If you are running this lesson from main.py, the '.venv' might already exist.")
    print("You would typically run this command once per project:")
    print("  python -m venv .venv")
    print("This creates a '.venv' directory containing a copy of the Python interpreter,")
    print("the pip package manager, and other supporting files.")
    print("\nNote: The `main.py` script usually runs lessons from the main interpreter,")
    print("not necessarily from inside the virtual environment itself.")
    print("For full demonstration, you would execute these steps in your terminal.")
    print("-" * 20)

    # 3. Activating a Virtual Environment
    # Activation adds the virtual environment's Python and pip to your PATH.

    print("\n--- 3. Activating a Virtual Environment ---")
    print("After creating, you need to activate it to use its isolated packages.")
    print("Open your terminal and navigate to this project's root directory.")
    print("Then, run one of the following commands:")
    print("  Windows (Command Prompt): .\.venv\Scripts\activate.bat")
    print("  Windows (PowerShell): .\.venv\Scripts\Activate.ps1")
    print("  macOS/Linux (Bash/Zsh): source ./.venv/bin/activate")
    print("\nOnce activated, your terminal prompt will usually change (e.g., to '(.venv) user@host...')")
    print("This indicates you are now operating within the virtual environment.")
    print("-" * 20)

    # 4. requirements.txt
    # This file lists all the Python packages (and their versions) required by your project.
    # It's essential for sharing your project and ensuring reproducibility.

    print("\n--- 4. Managing Dependencies with requirements.txt ---")
    print("Imagine your project uses 'requests' library.")
    print("To install it into your active virtual environment:")
    print("  pip install requests")
    print("\nTo generate a 'requirements.txt' file that lists all installed packages:")
    print("  pip freeze > requirements.txt")
    print("\nTo install all packages listed in 'requirements.txt' into a new environment:")
    print("  pip install -r requirements.txt")

    print("\nExample: Let's try to install 'requests' if it's not already installed.")
    try:
        import requests
        print("  'requests' library is already available.")
    except ImportError:
        print("  'requests' not found. This lesson cannot demonstrate installation directly.")
        print("  Please manually activate your virtual environment and run 'pip install requests'")
        print("  Then re-run this lesson from main.py to see the usage example.")
        print("  (Note: You might need to add 'requests' to the project's requirements.txt first if it's not there.)")
        print("-" * 20)
        print("--- End of Lesson (Please follow manual steps) ---")
        return

    # 5. Using a Package (e.g., requests) from the virtual environment
    # This part assumes 'requests' is installed in the environment where this script runs.
    print("\n--- 5. Using 'requests' library (from within an activated venv) ---")
    try:
        response = requests.get('https://api.github.com')
        print(f"  Successfully made an HTTP GET request to GitHub API.")
        print(f"  Status Code: {response.status_code}")
    except Exception as e:
        print(f"  Error using 'requests': {e}")
        print("  Ensure 'requests' is installed in your active virtual environment.")
    print("-" * 20)

    # 6. Deactivating a Virtual Environment
    # To exit the virtual environment and return to your system's global Python.

    print("\n--- 6. Deactivating a Virtual Environment ---")
    print("When you are done working in a virtual environment, you can deactivate it:")
    print("  deactivate")
    print("Your terminal prompt will return to its normal state.")
    print("-" * 20)

    utils.show_base_name(__file__, False)

if __name__ == "__main__":
    main()
else:
    utils.show_base_name(__file__, False)