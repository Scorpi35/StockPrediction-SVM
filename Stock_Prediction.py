import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import csv

file_name = "MSFT_Data2.csv"

class Loading_Data():

    def __init__(self):
        self.columns = "index".split()
        self.msft = pd.read_csv(file_name)
        self.df = pd.DataFrame(self.msft, columns=self.columns)

    def splitting_data(self, y):
        X_train, X_test, y_train, y_test = train_test_split(self.df, y, test_size=0.2)
        return X_train, y_train, y_train, y_test


class SVR_Model():

    def __init__(self):

        # Different Support Vector Regression model
        # We have used svr_poly, which is polynomial regression model
        self.svr_poly = SVR(kernel='poly', C=1e3, degree=2)
        self.svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
        self.svr_lin = SVR(kernel='linear', C=1e3)


class Prediction():

    def __init__(self):
        self.svr_obj = SVR_Model()
        self.svr_model_lin = self.svr_obj.svr_lin
        self.svr_model_poly = self.svr_obj.svr_poly
        self.svr_model_rbf = self.svr_obj.svr_rbf
        self.loading_data = Loading_Data()

    # Function for predicting closing price
    def preidict_close(self):
        y = self.loading_data.msft.close
        X_train, X_test, y_train, y_test = self.loading_data.splitting_data(y)
        y_poly = self.svr_model_poly.fit(X_train, y_train)
        close_prediction = self.svr_model_poly.predict(X_test)
        return

    # Function for predicting highest price
    def predict_high(self):
        y = self.loading_data.msft.high
        X_train, X_test, y_train, y_test = self.loading_data.splitting_data(y)
        y_poly = self.svr_model_poly.fit(X_train, y_train)
        high_prediction = self.svr_model_poly.predict(X_test)
        return

    # Function for predicting lowest price
    def predict_low(self):
        y = self.loading_data.msft.low
        X_train, X_test, y_train, y_test = self.loading_data.splitting_data(y)
        y_poly = self.svr_model_poly.fit(X_train, y_train)
        low_prediction = self.svr_model_poly.predict(X_test)
        return

    # Function for predicting volume
    def predict_volumne(self):
        y = self.loading_data.msft.volume
        X_train, X_test, y_train, y_test = self.loading_data.splitting_data(y)
        y_poly = self.svr_model_poly.fit(X_train, y_train)
        volume_prediction = self.svr_model_poly.predict(X_test)
        return


# The main function
if __name__ == "__main__":
    # Creating classes objects
    prediction = Prediction()

    # Function closing price
    prediction.predict_close()

    # Function opening price
    prediction.predict_hight()

    # Function highest price
    prediction.predict_high()

    # Function volume
    prediction.predict_volume()
