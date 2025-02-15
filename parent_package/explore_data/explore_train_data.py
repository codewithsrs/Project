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

train_path = os.path.join(path_dowload,'train.csv')
logging.info(f"Train data path: {train_path}")

try:
    train = pd.read_csv(train_path)
    train = train.drop('id', axis = 1)
    logging.info("Train data loaded and 'id' column dropped.")
except FileNotFoundError:
    logging.error(f"Train data file not found at: {train_path}")
    sys.exit(1)
except Exception as e:
    logging.error(f"Error loading train data: {e}")
    sys.exit(1)

extra_train_path = os.path.join(path_dowload,'training_extra.csv')
logging.info(f"Extra train data path: {extra_train_path}")

try:
    extra_train = pd.read_csv(extra_train_path)
    extra_train = extra_train.drop('id', axis = 1)
    logging.info("Extra train data loaded and 'id' column dropped.")
except FileNotFoundError:
    logging.error(f"Extra train data file not found at: {extra_train_path}")
    sys.exit(1)
except Exception as e:
    logging.error(f"Error loading extra train data: {e}")
    sys.exit(1)

try:
    train_total = pd.concat((train,extra_train)).drop_duplicates()
    logging.info("Train and extra train data concatenated and duplicates dropped.")
except Exception as e:
    logging.error(f"Error concatenating data: {e}")
    sys.exit(1)

def train_trans():
    try:
        from parent_package.explore_data.helper_func import replace_nan_values
        from pathlib import Path
        logging.info("Imported helper functions and Path successfully.")

        logging.info(f"Shape of combined dataframe: {train_total.shape}")

        col_containing_blank_values = train_total.isnull().sum().index
        logging.info(f"Columns containing blank values: {col_containing_blank_values}")

        logging.info("Information about dataset train_total:")
        logging.info(f"Data types:\n{train_total.dtypes}")
        logging.info(f"Number of null values per column before replacement:\n{train_total.isnull().sum()}")

        logging.info("Replacing null values...")
        for columns in col_containing_blank_values:
            replace_nan_values(train_total,columns)
            logging.info(f"Replaced NaN values in column: {columns}")

        logging.info("After replacing null values:")
        logging.info(f"Number of null values per column after replacement:\n{train_total.isnull().sum()}")

        logging.info(f"First few rows of transformed data:\n{train_total.head().to_string()}")

        return train_total
    except ImportError as e:
        logging.error(f"Import error in train_trans: {e}")
        return None
    except Exception as e:
        logging.error(f"Error in train_trans function: {e}")
        return None

try:
    transformed_train = train_trans()
    if transformed_train is not None:
        logging.info("Train data transformation completed successfully.")
        logging.info(f"Transformed train data shape: {transformed_train.shape}")
    else:
        logging.warning("Train data transformation returned None. Check for errors.")
except Exception as e:
    logging.error(f"An error occurred outside the train_trans function: {e}")