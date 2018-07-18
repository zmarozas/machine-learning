import pandas as pd
import numpy
def split_to_train_val_test(self, data):
    train_start = pd.to_datetime('2003-01-22')
    validation_start = pd.to_datetime('2016-01-01')
    test_start = pd.to_datetime('2017-01-01')
    train_data_mask = (train_start <= data['date']) & (data['date'] < validation_start)
    validation_data_mask = (validation_start <= data['date']) & (data['date'] < test_start)
    test_data_mask = (test_start <= data['date']) & (data['date'] < pd.to_datetime('today'))
    train_data = data.loc[train_data_mask]
    validation_data = data.loc[validation_data_mask]
    test_data = data.loc[test_data_mask]
return train_data, validation_data, test_data
