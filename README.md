#  Automated Directory Organizer

| Status: Complete | Language: Python 3.x | Category: Automation/Utility |
| :--- | :--- | :--- |

This is a single-script Python utility designed to automatically organize the contents of any specified directory into subfolders based on file type (e.g., Images, Documents, Code). It demonstrates practical scripting, robust I/O handling, and essential file system management.

##  Key Skills Demonstrated

* **File System Automation (I/O):** Utilizes Python's `os` and `shutil` libraries for low-level file path manipulation (`os.path.join`, `os.makedirs`) and reliable file movement (`shutil.move`).
* **Data-Driven Configuration:** The organization rules are defined entirely within a configurable `file_types` dictionary, allowing for easy expansion and maintenance.
* **Defensive Programming:** Implements **`try...except`** blocks to handle common runtime errors, such as invalid directory paths and file permission errors, ensuring the script is robust.
* **Path Manipulation:** Uses `os.path.splitext` and string methods to accurately parse file extensions and determine the correct destination.

---

## How It Works

The script follows a clear, two-stage process:

1.  **Preparation:**
    * Accepts a directory path from the user.
    * Creates all necessary destination folders (`Images`, `Documents`, etc.) using `os.makedirs(..., exist_ok=True)`.
2.  **Execution:**
    * Iterates through every item in the source directory using `os.listdir()`.
    * Bypasses directories (`os.path.isdir(...)`).
    * Matches the file extension against the `file_types` dictionary.
    * Moves the file to the corresponding folder (or to a `Misc` folder if the type is unknown) using `shutil.move()`.

---

## Setup and Usage

### Prerequisites
* Python 3.x (No external libraries required.)

### Running the Script
1.  Save the code as **`file_organizer.py`**.
2.  Open your terminal or command prompt.
3.  Run the script:
    ```bash
    python file_organizer.py
    ```
4.  The script will prompt you to enter the full path of the directory you wish to organize.