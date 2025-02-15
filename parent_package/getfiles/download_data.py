import connect_kaggle_api as k, Download_zip as d
import sys
import logging

logging.basicConfig(filename='main_script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Script execution started.")

logging.info(f"Python paths: {sys.path}")  # Log the paths

kg2 = k.kaggle_auth()
logging.info("Kaggle authentication object created.")

download_path = r'd:\BagPricePrediction\Project\data'
logging.info(f"Download path set to: {download_path}")

try:
    kg2.download(download_path,"playground-series-s5e2")
    logging.info("Kaggle competition files downloaded.")
except Exception as e:
    logging.error(f"Error during download: {e}")

try:
    d.extract_all_zips_in_directory(download_path)
    logging.info("ZIP files extracted.")
except Exception as e:
    logging.error(f"Error during ZIP extraction: {e}")

logging.info("Script execution finished.")