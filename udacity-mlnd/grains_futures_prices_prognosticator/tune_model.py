from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from matplotlib import pyplot
from pandas import DataFrame
from numpy import array

def fit_memmory_cels_model(n_cells,train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(n_cells, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    model.fit(train_X, train_y, epochs=150, batch_size=32, validation_data=(validation_X, validation_y), verbose=0, shuffle=False)
    loss= model.evaluate(validation_X, validation_y, verbose=0)
    return loss

def tune_memmory_cels(train_X,train_y,validation_X,validation_y):
    # define scope of search
    params = [1, 5, 10, 25, 50,100,200]
    n_repeats = 5
    # grid search parameter values
    scores = DataFrame()
    for value in params:
        # repeat each experiment multiple times
        loss_values = list()
        for i in range(n_repeats):
            loss = fit_memmory_cels_model(value,train_X,train_y,validation_X,validation_y)
            loss_values.append(loss)
            print('>%d/%d param=%f, loss=%f' % (i+1, n_repeats, value, loss))
        # store results for this parameter
        scores[str(value)] = loss_values
    # summary statistics of results
    print(scores.describe())
    # box and whisker plot of results
    scores.boxplot()
    pyplot.show()