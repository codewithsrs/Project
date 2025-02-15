from parent_package.modelling import Preprocessing
x_train,y_train, test, sc = Preprocessing.preprocess()

print(x_train.shape, y_train.shape)

from xgboost import XGBRegressor

xg = XGBRegressor(random_state = 3,n_estimators = 500,max_depth = 6,growpolicy = 'lossguide')

xg = xg.fit(x_train, y_train)


predicts = xg.predict(test)


print(sc.inverse_transform(predicts.reshape(-1,1))[:10])

