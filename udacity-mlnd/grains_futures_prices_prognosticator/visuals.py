###########################################
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
###########################################

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly.tools as tls

import pandas as pd
import numpy as np

def plot_lstm_prediction(actual, prediction, title='Google Trading vs Prediction', y_label='Price USD', x_label='Trading Days'):
    """
    Plots train, test and prediction
    :param actual: DataFrame containing actual data
    :param prediction: DataFrame containing predicted values
    :param title:  Title of the plot
    :param y_label: yLabel of the plot
    :param x_label: xLabel of the plot
    :return: prints a Pyplot againts items and their closing value
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Add labels
    plt.ylabel(y_label)
    plt.xlabel(x_label)

    # Plot actual and predicted close values

    plt.plot(actual, '#00FF00', label='Adjusted Close')
    plt.plot(prediction, '#0000FF', label='Predicted Close')

    # Set title
    ax.set_title(title)
    ax.legend(loc='upper left')
    plt.show()

def plot_original_price_series(df_fut_orig):
    """
    Plots Original Corn Futures Price Series using Plotly
    """

    fig = tls.make_subplots(rows=5, cols=1, shared_xaxes=True,print_grid=False, specs=[[{'rowspan': 4}],[None],[None],[None],[{}]]   )

    for col in ['Settle']:
        fig.append_trace({'x': df_fut_orig.index, 'y': df_fut_orig[col], 'type': 'scatter', 'name': col}, 1, 1)
    for col in ['Volume' ]:
        fig.append_trace({'x': df_fut_orig.index, 'y': df_fut_orig[col], 'type': 'bar', 'name': col}, 5, 1)
        
    fig['layout']['xaxis'].update(title='Date')
    fig['layout']['yaxis1'].update(title='Settling Price (Cents) ')
    fig['layout']['yaxis2'].update(title='Volume')
    cf.iplot(fig)



def plot_weekly_combined_series_by_date(df_weekly):
    """
    Plots weekly combined series (price series and cot report) using Plotly
    """

    fig = tls.make_subplots(rows=5, cols=1, shared_xaxes=True,print_grid=False,
                       specs=[[{'rowspan': 2}],[None],[{'rowspan': 2}],[None],[{}]]   )

    for col in ['Settle']:
        fig.append_trace({'x': df_weekly['Date'], 'y': df_weekly[col], 'type': 'scatter', 'name': col}, 1, 1)
    for col in ['Open_Interest','Longs','Shorts']:
        fig.append_trace({'x': df_weekly['Date'], 'y': df_weekly[col], 'type': 'scatter', 'name': col}, 3, 1)
        
    for col in ['Volume' ]:
        fig.append_trace({'x': df_weekly['Date'], 'y': df_weekly[col], 'type': 'bar', 'name': col}, 5, 1)
        
    fig['layout']['xaxis'].update(title='Date')
    fig['layout']['yaxis1'].update(title='Price (Cents)')
    fig['layout']['yaxis2'].update(title='Open Interest')
    fig['layout']['yaxis3'].update(title='Volume')
    cf.iplot(fig)

def plot_weekly_combined_series_by_trading_week(df_weekly):
    """
    Plots weekly combined series (price series and cot report) using Plotly. Use trading weeks on X axis
    """

    fig = tls.make_subplots(rows=5, cols=1, shared_xaxes=True,print_grid=False,
                       specs=[[{'rowspan': 2}],[None],[{'rowspan': 2}],[None],[{}]]   )

    for col in ['Settle']:
        fig.append_trace({'x': df_weekly.index, 'y': df_weekly[col], 'type': 'scatter', 'name': col}, 1, 1)
    for col in ['Open_Interest','Longs','Shorts']:
        fig.append_trace({'x': df_weekly.index, 'y': df_weekly[col], 'type': 'scatter', 'name': col}, 3, 1)
        
    for col in ['Volume' ]:
        fig.append_trace({'x': df_weekly.index, 'y': df_weekly[col], 'type': 'bar', 'name': col}, 5, 1)
        
    fig['layout']['xaxis'].update(title='Trading Week')
    fig['layout']['yaxis1'].update(title='Price (Cents)')
    fig['layout']['yaxis2'].update(title='Open Interest')
    fig['layout']['yaxis3'].update(title='Volume')
    cf.iplot(fig)