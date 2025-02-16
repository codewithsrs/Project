import logging
import os
import pandas as pd
from parent_package.modelling import Preprocessing
from parent_package.getfiles import connect_kaggle_api as c
from parent_package.explore_data.explore_test import path_dowload
from xgboost import XGBRegressor

logging.basicConfig(filename='model_training.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Model training script started.")


# Create a StreamHandler to send logs to the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set the level for terminal output (can be different from file level)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))  # Use the same format as the file

# Get the root logger and add the handler
root_logger = logging.getLogger()
root_logger.addHandler(console_handler)

try:
    x_train, y_train, test, sc = Preprocessing.preprocess()
    logging.info("Data preprocessed.")
    logging.info(f"x_train shape: {x_train.shape}, y_train shape: {y_train.shape}")
except Exception as e:
    logging.error(f"Error during preprocessing: {e}")
    exit(1) # Exit if preprocessing fails

try:
    xg = XGBRegressor(random_state=3)
    logging.info("XGBoost Regressor initialized.")

    xg = xg.fit(x_train, y_train)
    logging.info("XGBoost Regressor trained.")
except Exception as e:
    logging.error(f"Error during model training: {e}")
    exit(1)

sample_sub = os.path.join(path_dowload,'sample_submission.csv')
logging.info(f"Sample submission file path: {sample_sub}")

try:
    sample = pd.read_csv(sample_sub)
    logging.info("Sample submission file loaded.")
except FileNotFoundError:
    logging.error(f"Sample submission file not found at: {sample_sub}")
    exit(1)
except Exception as e:
    logging.error(f"Error loading sample submission: {e}")
    exit(1)


try:
    predicts = xg.predict(test)
    logging.info("Predictions generated.")

    sample['Price'] = sc.inverse_transform(predicts.reshape(-1,1))
    logging.info("Predictions added to sample submission DataFrame.")

    output_path = os.path.join(path_dowload,'submission.csv')
    sample.to_csv(output_path, index=False)
    logging.info(f"Predictions saved to: {output_path}")
except Exception as e:
    logging.error(f"Error during prediction or saving: {e}")
    exit(1)

try:
    c.kaggle_auth().submit_predictions(os.path.join(path_dowload,'submission.csv'),"VS Code Submission","playground-series-s5e2")
    logging.info("Predictions submitted to Kaggle.")
except Exception as e:
    logging.error(f"Error during Kaggle submission: {e}")

logging.info("Model training script finished.")