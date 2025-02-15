import numpy as np
import pandas as pd
import logging

logging.basicConfig(filename='my_log_file.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def replace_nan_values(df, col):
    try:
        if pd.api.types.is_numeric_dtype(df[col]):
            q25 = df[col].quantile(0.25)
            q75 = df[col].quantile(0.75)
            logging.info(f'{col},{q25},{q75}')
            df.fillna({col:(q25 + q75) / 1.5}, inplace=True)
            logging.info(f"Replaced NaN values in numeric column '{col}' using calculated value.")
        elif pd.api.types.is_object_dtype(df[col]):
            unique_vals = df[col].dropna().unique()
            if len(unique_vals) > 0:
                df[col] = np.where(df[col].isna(),np.random.choice(unique_vals),df[col])
                logging.info(f"Replaced NaN values in object column '{col}' with random choice from existing values.")
            else:
                logging.warning(f"Column '{col}' contains only null values. No replacement possible.")
        else:
            logging.warning(f"Column '{col}' is of an unhandled data type. No replacement performed.")
    except Exception as e:
        logging.error(f"Error in replace_nan_values for column '{col}': {e}")