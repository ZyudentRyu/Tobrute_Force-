# Tobrute_Force
**Tobrute_Force** is a brute force tool to crack passwords on **ZIP**, **RAR**, and **TAR** files using a provided wordlist. It supports multiple file formats and shows the progress of each password attempt. Run it with Python to try different passwords from a wordlist to unlock protected files.

## Features:
- Supports **ZIP**, **RAR**, and **TAR** file formats.
- Attempts password cracking using brute force and a provided wordlist.
- Displays clear output for each password attempted.

## Installation:

### **1. Using a Virtual Environment (Recommended)**

To avoid potential issues with system-wide Python packages, it's recommended to use a virtual environment:

1. **Create a virtual environment**:
    ```bash
    python3 -m venv myenv
    ```

2. **Activate the virtual environment**:
    ```bash
    source myenv/bin/activate
    ```

3. **Install required dependencies**:
    - To install **`rarfile`** and other dependencies:
    ```bash
    pip install rarfile
    ```

### **2. Install Dependencies Globally (If Not Using Virtual Environment)**

If you choose not to use a virtual environment, you can install **`rarfile`** globally with:
    ```bash
    pip3 install rarfile
    ```

### **3. Run the Script**

Once dependencies are installed, run the script:
    ```bash
    python3 tobrute.py
    ```

## Usage:
To use this tool, provide the file path to a password-protected **ZIP**, **RAR**, or **TAR** file and the path to your wordlist file.

