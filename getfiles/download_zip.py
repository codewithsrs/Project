from connect_kaggle_api import  kaggle_auth
import os
import zipfile


kg2 = kaggle_auth()

def download_data(path,name):
    kg2.download(path,name)

def extract_and_delete_zip(zip_filepath, extract_to_dir):
    """Extracts files from a zip archive and then deletes the zip file.

    Args:
        zip_filepath: The path to the zip file.
        extract_to_dir: The directory where the extracted files should be placed.
    """

    try:
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)  # Extract all files
        print(f"Successfully extracted files from '{zip_filepath}' to '{extract_to_dir}'.")

        os.remove(zip_filepath)  # Delete the zip file
        print(f"Successfully deleted zip file: '{zip_filepath}'.")

    except FileNotFoundError:
        print(f"Error: Zip file '{zip_filepath}' not found.")
    except zipfile.BadZipFile:
        print(f"Error: Invalid zip file format: '{zip_filepath}'.")
    except OSError as e:  # Handle potential OS errors (permissions, etc.)
        print(f"Error: An OS error occurred: {e}")
    except Exception as e: # Catch any other exception
        print(f"An unexpected error occurred: {e}")



# Example with a directory that may contain zip files:
def extract_all_zips_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            zip_path = os.path.join(directory, filename)
            extract_path = os.path.join(directory, filename[:-4]) # Extract to a directory with the same name as the zip file (without .zip)
            os.makedirs(extract_path, exist_ok=True)
            extract_and_delete_zip(zip_path, extract_path)
