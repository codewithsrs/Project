import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys
import importlib
import logging

logging.basicConfig(filename='my_log_file.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

path_dowload = r'd:\BagPricePrediction\Project\data'

test_path = os.path.join(path_dowload,'test.csv')

logging.info(f"Test data path: {test_path}")

try:
    test = pd.read_csv(test_path)
    logging.info("Test data loaded successfully.")
except FileNotFoundError:
    logging.error(f"Test data file not found at: {test_path}")
    sys.exit(1)
except Exception as e:
    logging.error(f"Error loading test data: {e}")
    sys.exit(1)

test = test.drop('id', axis = 1)
logging.info("Dropped 'id' column from test data.")

def test_trans():
    try:
        from parent_package.explore_data import helper_func as h
        from pathlib import Path
        logging.info("Imported helper functions and Path successfully.")

        for col in test.columns:
            h.replace_nan_values(test,col)
            logging.info(f"Replaced NaN values in column: {col}")

        return test
    except ImportError as e:
        logging.error(f"Import error in test_trans: {e}")
        return None
    except Exception as e:
        logging.error(f"Error in test_trans function: {e}")
        return None

try:
    transformed_test = test_trans()
    if transformed_test is not None:
        logging.info("Test data transformation completed successfully.")
        logging.info(f"Transformed test data shape: {transformed_test.shape}")
    else:
        logging.warning("Test data transformation returned None. Check for errors.")
except Exception as e:
    logging.error(f"An error occurred outside the test_trans function: {e}")