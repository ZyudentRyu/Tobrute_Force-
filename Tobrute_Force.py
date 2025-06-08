import zipfile
import rarfile
import tarfile

# Adding the script's logo or name with a symbol
def print_logo():
    logo = """
    *******************************
    *     Tobrute_Force          *
    *        -_-                 *
    *******************************
    """
    print(logo)

def extract_zip(zipfile_path, password):
    """
    Try to extract a ZIP file with the given password.
    
    :param zipfile_path: Path to the password-protected ZIP file
    :param password: The password being tested
    :return: True if successful, False if failed
    """
    try:
        with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
            zip_ref.extractall(pwd=password.encode())
            print(f"Password found (ZIP): {password}")
            return True
    except (RuntimeError, zipfile.BadZipFile):
        return False

def extract_rar(rarfile_path, password):
    """
    Try to extract a RAR file with the given password.
    
    :param rarfile_path: Path to the password-protected RAR file
    :param password: The password being tested
    :return: True if successful, False if failed
    """
    try:
        with rarfile.RarFile(rarfile_path) as rar_ref:
            rar_ref.extractall(pwd=password)
            print(f"Password found (RAR): {password}")
            return True
    except (rarfile.BadRarFile, RuntimeError):
        return False

def extract_tar(tarfile_path, password):
    """
    Try to extract a TAR file with the given password.
    
    :param tarfile_path: Path to the password-protected TAR file
    :param password: The password being tested
    :return: True if successful, False if failed
    """
    try:
        with tarfile.open(tarfile_path) as tar_ref:
            tar_ref.extractall()
            print(f"Password found (TAR): {password}")
            return True
    except Exception as e:
        return False

def brute_force(file_path, file_type, wordlist_path):
    """
    Function to try each password in the wordlist to open various types of files.

    :param file_path: Path to the password-protected file
    :param file_type: File type (zip, rar, tar)
    :param wordlist_path: Path to the wordlist file containing the list of passwords
    """
    with open(wordlist_path, 'r') as wordlist:
        for line in wordlist:
            password = line.strip()  # Take the password from the wordlist
            print(f"Trying password: {password}")
            
            if file_type == "zip":
                if extract_zip(file_path, password):
                    break
            elif file_type == "rar":
                if extract_rar(file_path, password):
                    break
            elif file_type == "tar":
                if extract_tar(file_path, password):
                    break
            else:
                print(f"File format {file_type} not supported.")
                break

# Display the logo with a symbol
print_logo()

# User input
file_path = input("Enter the path to the password-protected file: ")
file_type = input("Enter the file type (zip/rar/tar): ").lower()
wordlist_path = input("Enter the path to the wordlist file (e.g., wordlist.txt): ")

# Run brute force
brute_force(file_path, file_type, wordlist_path)
