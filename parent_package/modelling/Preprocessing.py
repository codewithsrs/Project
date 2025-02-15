def preprocess():

    from parent_package.explore_data.explore_train_data import train_trans
    from parent_package.explore_data.explore_test import test_trans
    from sklearn.preprocessing import LabelEncoder, StandardScaler
    from parent_package.explore_data.helper_func import replace_nan_values
    import pandas as pd


    train_total = train_trans()
    test = test_trans()


    x_train = train_total.drop('Price', axis = 1)
    y_train = train_total[['Price']]

    cat_cols = [i for i in x_train.columns if pd.api.types.is_object_dtype(x_train[i])]
    for i in cat_cols:
        print(f'train is having {x_train[i].nunique()} values and values are {x_train[i].unique()}')
        print(f'test is having {test[i].nunique()} values and values are {test[i].unique()} \n\n')


    le = LabelEncoder()
    sc = StandardScaler()

    for i in cat_cols:
        x_train[i] = le.fit_transform(x_train[i])
        test[i] = le.transform(test[i])
    
    x_train = sc.fit_transform(x_train)
    test = sc.transform(test)
    y_train = sc.fit_transform(y_train)

    return x_train, y_train, test, sc







# from xgboost import XGBRegressor

# xg = XGBRegressor(random_state = 3,n_estimators = 500,max_depth = 6,growpolicy = 'lossguide')