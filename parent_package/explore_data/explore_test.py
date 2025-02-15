def test_trans():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import os
    import sys
    import importlib
    from parent_package.explore_data import  helper_func as h
    from pathlib import Path
    path_dowload = r'd:\BagPricePrediction\Project\data'

    test_path = os.path.join(path_dowload,'test.csv')
    test = pd.read_csv(test_path)
    test = test.drop('id', axis = 1)
    for col in test.columns:
        h.replace_nan_values(test,col)

    return test
    # train_total.head()
    # from xgboost import XGBRegressor

    # xg = XGBRegressor(random_state = 3,n_estimators = 500,max_depth = 6,growpolicy = 'lossguide')


    print(test.isnull().sum())