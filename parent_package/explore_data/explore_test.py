import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys
import importlib
path_dowload = r'd:\BagPricePrediction\Project\data'

test_path = os.path.join(path_dowload,'test.csv')
test = pd.read_csv(test_path)
test = test.drop('id', axis = 1)

def test_trans():

    from parent_package.explore_data import  helper_func as h
    from pathlib import Path

    for col in test.columns:
        h.replace_nan_values(test,col)

    return test
    # train_total.head()
