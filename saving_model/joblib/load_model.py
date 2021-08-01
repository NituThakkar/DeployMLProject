import joblib

model = joblib.load('saving_model/joblib/dib_79.pkl')

output = model.predict([[1,2,3,4,5,6,7,8]])

if output[0] == 1:
    print('diabatic')
else:
    print('not diabatic')
