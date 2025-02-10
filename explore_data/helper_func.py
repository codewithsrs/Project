import numpy as np




def replace_Nan_values(df,col):
    """
    This function is designed to replace null values, with some random 
    values picked from the unique values of the same column.
    """

    if df[col].dtypes != 'O':

        upper = np.percentile(0.75,df[col])
        lower = np.percentile(0.35,df[col])

        df[col] = np.where(df[col].isna(),np.random.randint(lower,upper),\
                                df[col])
    else:

        unique_values_in_col = df[df[col].notna()][col].unique()

        df[col] = np.where(df[col].isna(),np.random.choice(unique_values_in_col),\
                                    df[col])