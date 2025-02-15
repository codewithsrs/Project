import logging
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

logging.basicConfig(filename='preprocess.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess():
    try:
        from parent_package.explore_data.explore_train_data import train_trans
        from parent_package.explore_data.explore_test import test_trans
        logging.info("Imported necessary modules.")

        train_total = train_trans()
        test = test_trans()
        logging.info("Train and test data loaded and transformed.")

        x_train = train_total.drop('Price', axis=1)
        y_train = train_total[['Price']]
        logging.info("Split train data into features (x_train) and target (y_train).")

        cat_cols = [i for i in x_train.columns if pd.api.types.is_object_dtype(x_train[i])]
        logging.info(f"Categorical columns: {cat_cols}")

        for i in cat_cols:
            logging.info(f'Train column {i} has {x_train[i].nunique()} unique values: {x_train[i].unique()}')
            logging.info(f'Test column {i} has {test[i].nunique()} unique values: {test[i].unique()}')

        le = LabelEncoder()
        sc = StandardScaler()
        logging.info("LabelEncoder and StandardScaler initialized.")

        for i in cat_cols:
            x_train[i] = le.fit_transform(x_train[i])
            test[i] = le.transform(test[i])
            logging.info(f"Encoded categorical column: {i}")

        x_train = sc.fit_transform(x_train)
        test = sc.transform(test)
        y_train = sc.fit_transform(y_train)
        logging.info("Scaled features (x_train, test) and target (y_train).")

        logging.info("Preprocessing completed.")
        return x_train, y_train, test, sc

    except ImportError as e:
        logging.error(f"Import error in preprocess: {e}")
        return None, None, None, None  # Or handle differently
    except Exception as e:
        logging.error(f"Error in preprocess function: {e}")
        return None, None, None, None