import os
import zipfile
import logging

logging.basicConfig(filename='zip_extraction.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def extract_and_delete_zip(zip_filepath, extract_to_dir):
    try:
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)
        logging.info(f"Successfully extracted files from '{zip_filepath}' to '{extract_to_dir}'.")

        os.remove(zip_filepath)
        logging.info(f"Successfully deleted zip file: '{zip_filepath}'.")

    except FileNotFoundError:
        logging.error(f"Error: Zip file '{zip_filepath}' not found.")
    except zipfile.BadZipFile:
        logging.error(f"Error: Invalid zip file format: '{zip_filepath}'.")
    except OSError as e:
        logging.error(f"Error: An OS error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


def extract_all_zips_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            zip_path = os.path.join(directory, filename)
            os.makedirs(directory, exist_ok=True)
            extract_and_delete_zip(zip_path, directory)