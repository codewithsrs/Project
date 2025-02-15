from parent_package.explore_data.explore_train_data import train_trans
from parent_package.explore_data.explore_test import test_trans
from sklearn.preprocessing import LabelEncoder
from parent_package.explore_data.helper_func import replace_nan_values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


train_total = train_trans()
test = test_trans()


x_train = train_total.drop('Price', axis = 1)
y_train = train_total['Price']


cat_cols = [i for i in x_train.columns if pd.api.types.is_object_dtype(x_train[i])]
le = LabelEncoder()



# from xgboost import XGBRegressor

# xg = XGBRegressor(random_state = 3,n_estimators = 500,max_depth = 6,growpolicy = 'lossguide')