import os
from kaggle import api
import logging

logging.basicConfig(filename='kaggle_auth.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class kaggle_auth:
    def __init__(self):
        logging.info("kaggle_auth object initialized.")

    @staticmethod  
    def authenticate_key():
        try:
            api.authenticate()
            logging.info("Kaggle API authenticated successfully.")
        except Exception as e:
            logging.error(f"Error during Kaggle authentication: {e}")

    def download(self, path, name):
        self.path = path
        self.name = name
        try:
            if not os.path.exists(self.path):
                os.makedirs(self.path, exist_ok=True)
                logging.info(f"Successfully created directory: {self.path}")
            api.competition_download_files(self.name, path=self.path, quiet=False)
            logging.info(f"Competition files downloaded to: {self.path}")
        except Exception as e:
            logging.error(f"Error downloading competition files: {e}")

    def list_files(self, name):
        self.name = name
        try:
            file_list = api.competitions_list(search=self.name)
            logging.info(f"Competition files listed for: {self.name}")
            return file_list
        except Exception as e:
            logging.error(f"Error listing competition files: {e}")
            return None  # Return None in case of error

    def submit_predictions(self, filename, msg, comp_name):
        self.filename = filename
        self.msg = msg
        self.comp_name = comp_name
        try:
            api.competition_submit(self.filename,msg,comp_name)
            logging.info(f"Predictions submitted for file: {self.filename}")
        except Exception as e:
            logging.error(f"Error submitting predictions: {e}")