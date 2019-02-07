import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pickle
from copy import deepcopy

dataset_train = pd.read_csv('MSFT_Data.csv')
training_set = dataset_train.iloc[:, 1:2].values
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

X_test = []

for i in range(60, 100):

    X_test = []

    df = pd.read_csv('Sample_Stock.csv')
    inputs = df.values
    inputs = inputs.reshape(-1, 1)
    inputs = sc.transform(inputs)

    X_test.append(inputs[i-60: i, 0])
    X_test1 = deepcopy(np.array(X_test))
    X_test1 = np.reshape(X_test1, (X_test1.shape[0], X_test1.shape[1], 1))
    open_name = "Predict_Open_Model1.sav"
    open_model = pickle.load(open(open_name, "rb"))

    predicted_value = open_model.predict(X_test1)
    predicted_value = sc.inverse_transform(predicted_value)

    b = predicted_value.ravel()
    b = float(b)

    df.loc[i + 1] = [b]
    df.to_csv('Sample_Stock.csv', index=False)




