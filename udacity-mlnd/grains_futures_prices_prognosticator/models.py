from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
# persistence model
def model_persistence(x):
    return x
    
def basic_lstm_model(train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(1, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history = model.fit(train_X, train_y, epochs=150, batch_size=32, validation_data=(validation_X, validation_y), verbose=2, shuffle=False)
    return model,history.history


def improoved_lstm_model(train_X,train_y,validation_X,validation_y):
    model = Sequential()
    model.add(LSTM(10, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history = model.fit(train_X, train_y, epochs=150, batch_size=32, validation_data=(validation_X, validation_y), verbose=2, shuffle=False)
    return model,history.history
