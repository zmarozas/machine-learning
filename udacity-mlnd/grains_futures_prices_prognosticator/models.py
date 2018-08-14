from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras import  optimizers
from keras.regularizers import L1L2
from numpy import concatenate
from math import sqrt
from sklearn.metrics import mean_squared_error
# persistence model
def model_persistence(x):
    return x


def make_benchmark_model_prediction(bench_x,bench_y):
    # walk-forward validation
    predictions = list()
    for x in bench_x:
        yhat = model_persistence(x)
        predictions.append(yhat)
    rmse = sqrt(mean_squared_error(bench_y, predictions))
    return predictions,rmse


def make_lstm_prediction(x_data,y_data,model,scaler):
    # make a prediction
    yhat = model.predict(x_data)
    x_data_eval = x_data.reshape((x_data.shape[0], x_data.shape[2]))
    # invert scaling for forecast
    inv_yhat = concatenate((yhat, x_data_eval[:, 1:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:,0]
    # invert scaling for actual
    y_data_eval = y_data.reshape((len(y_data), 1))
    inv_y = concatenate((y_data_eval, x_data_eval[:, 1:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:,0]
    # calculate RMSE
    rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
    return inv_yhat, inv_y, rmse   


def basic_lstm_model(train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(1, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history = model.fit(train_X, train_y, epochs=500, batch_size=32, validation_data=(validation_X, validation_y), verbose=2, shuffle=False)
    return model,history.history


def improved_lstm_model(train_X,train_y,validation_X,validation_y):
    model = Sequential()
    reg = L1L2(l1=0.0, l2=0.01)
    model.add(LSTM(25, input_shape=(train_X.shape[1], train_X.shape[2]),bias_regularizer=reg))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history=model.fit(train_X, train_y, epochs=500, batch_size=128, validation_data=(validation_X, validation_y), verbose=2, shuffle=False)
    return model,history.history