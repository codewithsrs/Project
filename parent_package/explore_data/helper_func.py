import numpy as np




def replace_Nan_values(df,col):
    """
    This function is designed to replace null values, with some random 
    values picked from the unique values of the same column.
    """

    if df[col].dtypes != 'O':

        upper = np.percentile(df[col],75)
        lower = np.percentile(df[col],25)

        df[col] = np.where(df[col].isna(),(lower+upper)/1.5,\
                                df[col])
    else:

        unique_values_in_col = df[df[col].notna()][col].unique()

        df[col] = np.where(df[col].isna(),np.random.choice(unique_values_in_col),\
                                    df[col])