import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pd.read_csv(url,names=names)
print(df)

X = df.iloc[: , :8]
Y = df.iloc[: , 8]

X_train,X_test,Y_train,Y_test = model_selection.train_test_split(X,Y,test_size=0.2,random_state=101)

model = LogisticRegression()
model.fit(X_train,Y_train)
result = model.score(X_test,Y_test)
print(result)

pickle.dump(model,open('saving_model/pickle/dib_79.pkl','wb'))


