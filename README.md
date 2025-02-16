# Kaggle API Wrapper Class

This Python code defines a class `kaggle_auth` that provides a convenient interface for interacting with the Kaggle API.  It encapsulates common operations like authentication, downloading competition files, listing files, and submitting predictions.  The class also incorporates logging for tracking actions and errors.

## Class Overview

The `kaggle_auth` class simplifies Kaggle API interactions by providing methods for:

- **Authentication:** Authenticates with the Kaggle API using API key.
- **Downloading Files:** Downloads competition data files to a specified directory.
- **Listing Files:** Lists files associated with a given competition.
- **Submitting Predictions:** Submits prediction files to a competition.

## Class Methods

### `__init__(self)`

- Initializes a `kaggle_auth` object.
- Logs the object's initialization.

### `authenticate_key()` (Static Method)

- Authenticates with the Kaggle API using the `kaggle` library's `api.authenticate()` function.
- This is a static method as it doesn't require access to instance-specific data.
- Logs successful authentication or any errors encountered.

### `download(self, path, name)`

- Downloads competition files.
- `path`: The directory where files should be downloaded. If the directory doesn't exist, it's created.
- `name`: The name or ID of the Kaggle competition.
- Uses `api.competition_download_files()` to download the files.
- Logs the download process and any errors.

### `list_files(self, name)`

- Lists competition files.
- `name`: The name or ID of the Kaggle competition.
- Uses `api.competitions_list()` to retrieve the file list.
- Logs the listing operation and any errors.
- Returns the list of files or `None` if an error occurs.

### `submit_predictions(self, filename, msg, comp_name)`

- Submits predictions to a Kaggle competition.
- `filename`: The path to the prediction CSV file.
- `msg`: A message describing the submission.
- `comp_name`: The name or ID of the Kaggle competition.
- Uses `api.competition_submit()` to submit the predictions.
- Logs the submission process and any errors.

## Usage Example

```python
from kaggle_auth import kaggle_auth

# Initialize the Kaggle authentication class
kauth = kaggle_auth()

# Authenticate with Kaggle API
kauth.authenticate_key()

# Download competition files
kauth.download("data/house-prices", "house-prices-advanced-regression-techniques")

# List files for a competition (example)
files = kauth.list_files("house-prices-advanced-regression-techniques")
if files:
    for file in files:
        print(file)

# Submit predictions
kauth.submit_predictions("submission.csv", "My submission message", "house-prices-advanced-regression-techniques")








# Model Training Script

This script trains an XGBoost Regressor model for a playground competition (likely related to house prices, given the use of a `Price` column and a Kaggle submission). It includes data preprocessing, model training, prediction generation, and submission to Kaggle.  The script also incorporates robust logging to track progress and errors.

## Script Overview

The script performs the following steps:

1. **Imports:** Imports necessary libraries like `logging`, `os`, `pandas`, custom modules from a `parent_package` (including preprocessing and Kaggle interaction functions), and `XGBRegressor`.

2. **Logging Setup:** Configures logging to both a file (`model_training.log`) and the console.  This allows for detailed tracking of the script's execution.

3. **Data Preprocessing:** Calls the `Preprocessing.preprocess()` function to load and preprocess the training and test data.  It logs the shapes of the resulting `x_train` and `y_train`.  Error handling is included to catch and log any exceptions during preprocessing.  The script exits if preprocessing fails.

4. **Model Training:** Initializes an `XGBRegressor` with a random state for reproducibility.  Trains the model using the preprocessed training data.  Logs the initialization and training steps.  Includes error handling for training exceptions.

5. **Sample Submission Loading:** Loads the `sample_submission.csv` file. Logs the file path and loading status. Handles `FileNotFoundError` and other exceptions that might occur during file loading.

6. **Prediction Generation:** Generates predictions on the test data using the trained XGBoost model.  Inverse transforms the predictions using the scaler (`sc`) to get the actual prices. Adds the predicted prices to the sample submission DataFrame.  Logs these steps. Error handling is included.

7. **Submission File Saving:** Saves the updated sample submission DataFrame (containing the predictions) to a new CSV file named `submission.csv`. Logs the output path. Includes error handling for saving.

8. **Kaggle Submission:** Submits the `submission.csv` file to Kaggle using the `connect_kaggle_api.submit_predictions()` function.  Logs the submission attempt.  Includes error handling for Kaggle submission failures.

9. **Script Completion:** Logs the successful completion of the script.

## Dependencies

- `logging`
- `os`
- `pandas`
- `xgboost`
- Custom modules from `parent_package` (specifically `modelling` and `getfiles`)

## Usage

To run this script, ensure that the required libraries are installed and the `parent_package` is correctly configured and accessible.  The script expects a `sample_submission.csv` file and training/test data to be available.  The Kaggle API credentials should be set up for the submission step to work.

## Logging

The script utilizes logging to track progress and errors.  Logs are written to both a file (`model_training.log`) and the console.  The log messages include timestamps and log levels (INFO, ERROR).

## Error Handling

The script includes `try...except` blocks to handle potential errors during preprocessing, model training, file loading, prediction, saving, and Kaggle submission.  If an error occurs, it is logged, and the script may exit.

## File Structure (Illustrative)