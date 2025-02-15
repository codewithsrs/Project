def train_trans():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import os
    import sys
    import importlib
    from parent_package.explore_data.helper_func import replace_nan_values 
    from pathlib import Path
    path_dowload = r'd:\BagPricePrediction\Project\data'

    print("setting train path")
    train_path = os.path.join(path_dowload,'train.csv')


    print("Reading the training file..")
    train = pd.read_csv(train_path)
    train = train.drop('id', axis = 1)

    print("setting the original training data path for read..")
    extra_train_path = os.path.join(path_dowload,'training_extra.csv')

    print("Reading the original train data")
    extra_train = pd.read_csv(extra_train_path)
    extra_train = extra_train.drop('id', axis = 1)

    print("Concatinating the train and original training data....")
    train_total = pd.concat((train,extra_train)).drop_duplicates()

    print("Lets check the shape of combined dataframe")
    train_total.shape

    print("-----------------------------------------------------------------")
    col_containing_blank_values = train_total.isnull().sum().index

    print("Information about dataset train_total below \n\n")
    print(train_total.info())

    print("-----------------------------------------------------------")
    print(col_containing_blank_values)
    print("Replacing null values in next step...........Please wait")
    for columns in col_containing_blank_values:
        replace_nan_values(train_total,columns)
        
    print("After replacing lets check the information")
    print(train_total[col_containing_blank_values].isnull().sum())

    print(train_total.head())

    return train_total