import numpy as np
import pandas as pd

def replace_nan_values(df, col):
    if pd.api.types.is_numeric_dtype(df[col]):
        q25 = df[col].quantile(0.25)
        q75 = df[col].quantile(0.75)
        print(f'{col},{q25},{q75}')
        df.fillna({col:(q25 + q75) / 1.5}, inplace=True)
    elif pd.api.types.is_object_dtype(df[col]):
        unique_vals = df[col].dropna().unique()
        if len(unique_vals) > 0: # Handle all-NaN column case
            df[col] = np.where(df[col].isna(),np.random.choice(unique_vals),df[col])
        else:
            print(f"Warning: Column '{col}' contains only null values.  No replacement possible.")
    else:
        print(f"Warning: Column '{col}' is of an unhandled data type. No replacement performed.")
