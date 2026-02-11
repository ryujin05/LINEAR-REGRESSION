import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
model = joblib.load('house_model.pkl')
features = joblib.load('features_list.pkl')
df=pd.read_csv('train.csv')
features=['GrLivArea','BedroomAbvGr','FullBath','OverallQual']
X=df[features]
y=df['SalePrice']
X=X.fillna(X.median())
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=18)
model= LinearRegression()
model.fit(X_train,y_train)
y_predicted=model.predict(X_test)
mse=mean_squared_error(y_test,y_predicted)
print(f"Da huan luyen xong sai so MSE:{mse:.2f}")
joblib.dump(model,'house_model.pkl')
joblib.dump(features,'features_list.pkl')
