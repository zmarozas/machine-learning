from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras import  optimizers
from keras.regularizers import L1L2

from matplotlib import pyplot
from pandas import DataFrame
from numpy import array

def fit_memmory_cells_model(n_cells,train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(n_cells, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    model.fit(train_X, train_y, epochs=500, batch_size=64, validation_data=(validation_X, validation_y), verbose=0, shuffle=False)
    loss= model.evaluate(validation_X, validation_y, verbose=0)
    return loss

def tune_memmory_cells(train_X,train_y,validation_X,validation_y):
    # define scope of search
    params = [1, 5, 10, 25, 50,100,200]
    n_repeats = 5
    # grid search parameter values
    scores = DataFrame()
    for value in params:
        # repeat each experiment multiple times
        loss_values = list()
        for i in range(n_repeats):
            loss = fit_memmory_cells_model(value,train_X,train_y,validation_X,validation_y)
            loss_values.append(loss)
            print('>%d/%d param=%f, loss=%f' % (i+1, n_repeats, value, loss))
        # store results for this parameter
        scores[str(value)] = loss_values
    # summary statistics of results
    print(scores.describe())
    # box and whisker plot of results
    scores.boxplot()
    pyplot.show()


def fit_batch_size_model(n_batch,train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(25, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    model.fit(train_X, train_y, epochs=500, batch_size=n_batch, validation_data=(validation_X, validation_y), verbose=0, shuffle=False)
    loss= model.evaluate(validation_X, validation_y, verbose=0)
    return loss

def tune_batch_size(train_X,train_y,validation_X,validation_y):
    # define scope of search
    params = [2, 4, 8, 32, 64,128,256]
    n_repeats = 5
    # grid search parameter values
    scores = DataFrame()
    for value in params:
        # repeat each experiment multiple times
        loss_values = list()
        for i in range(n_repeats):
            loss = fit_batch_size_model(value,train_X,train_y,validation_X,validation_y)
            loss_values.append(loss)
            print('>%d/%d param=%f, loss=%f' % (i+1, n_repeats, value, loss))
        # store results for this parameter
        scores[str(value)] = loss_values
    # summary statistics of results
    print(scores.describe())
    # box and whisker plot of results
    scores.boxplot()
    pyplot.show()


def fit_learning_rate_model(n_rate,train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(25, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    optimizer = optimizers.Adam(lr=n_rate)

    model.compile(optimizer=optimizer,loss='mae')
    # fit network
    model.fit(train_X, train_y, epochs=500, batch_size=32, validation_data=(validation_X, validation_y), verbose=0, shuffle=False)
    loss= model.evaluate(validation_X, validation_y, verbose=0)
    return loss

def tune_learning_rate(train_X,train_y,validation_X,validation_y):
    # define scope of search
    params = [0.1,0.001,0.0001]
    n_repeats = 5
    # grid search parameter values
    scores = DataFrame()
    for value in params:
        # repeat each experiment multiple times
        loss_values = list()
        for i in range(n_repeats):
            loss = fit_learning_rate_model(value,train_X,train_y,validation_X,validation_y)
            loss_values.append(loss)
            print('>%d/%d param=%f, loss=%f' % (i+1, n_repeats, value, loss))
        # store results for this parameter
        scores[str(value)] = loss_values
    # summary statistics of results
    print(scores.describe())
    # box and whisker plot of results
    scores.boxplot()
    pyplot.show()


def fit_weight_regularization_model(reg,train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(25, input_shape=(train_X.shape[1], train_X.shape[2]),kernel_regularizer=reg))
    model.add(Dense(1))
    optimizer = optimizers.Adam(lr=0.001)

    model.compile(optimizer=optimizer,loss='mae')
    # fit network
    model.fit(train_X, train_y, epochs=500, batch_size=32, validation_data=(validation_X, validation_y), verbose=0, shuffle=False)
    loss= model.evaluate(validation_X, validation_y, verbose=0)
    return loss

def tune_weight_regularization(train_X,train_y,validation_X,validation_y):
    # define scope of search
    regularizers = {1:L1L2(l1=0.0, l2=0.01), 2:L1L2(l1=0.01, l2=0.0), 3:L1L2(l1=0.0, l2=0.0), 4:L1L2(l1=0.01, l2=0.01)}
    n_repeats = 5
    # grid search parameter values
    scores = DataFrame()
    for reg in regularizers.keys():
        # repeat each experiment multiple times
        loss_values = list()
        for i in range(n_repeats):
            loss = fit_weight_regularization_model(regularizers[reg],train_X,train_y,validation_X,validation_y)
            loss_values.append(loss)
            print('>%d/%d param=%f, loss=%f' % (i+1, n_repeats, reg, loss))
        # store results for this parameter
        scores[str(reg)] = loss_values
    # summary statistics of results
    print(scores.describe())
    # box and whisker plot of results
    scores.boxplot()
    pyplot.show()