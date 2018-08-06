
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import plotly.tools as tls

import pandas as pd
from pandas import Grouper
import numpy as np


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


def plot_series_to_compare(series1, series2, series1_name, series2_name,title):
    """
    Plots Two series for easy comparison
    """

    fig = tls.make_subplots(rows=1, cols=1, shared_xaxes=True,print_grid=False  )
    fig['layout'].update(height=400, width=899, title=title)

    x_series=np.arange(0,len(series1))

    fig.append_trace({'x': x_series, 'y': series1, 'type': 'scatter', 'name': series1_name}, 1, 1)
    fig.append_trace({'x': x_series, 'y': series2, 'type': 'scatter', 'name': series2_name}, 1, 1)

        
    fig['layout']['xaxis'].update(title='Trading Week')
    fig['layout']['yaxis'].update(title='Price (Cents)')
    cf.iplot(fig)

def plot_grouped_by_year_data(df_weekly,title):
    """
    Plots weekly combined series (price series and cot report) using Plotly. Use trading weeks on X axis
    """
    x_series=np.arange(0,54)
    groups = df_weekly['Settle'].groupby(Grouper(freq='A'))
    fig = tls.make_subplots(rows=len(groups), cols=1, shared_xaxes=True,print_grid=False )
    fig['layout'].update(height=600, width=899, title=title)
    for i,(name, group) in enumerate(groups):
        lst = map(lambda x: x, group.values)
        ser = pd.Series(lst)
        # chart only data where we have full year (52 weeks)
        if len(ser) >= 52:
            fig.append_trace({'x': x_series, 'y':  ser, 'type': 'scatter', 'name': name.year}, i+1, 1)
            fig['layout']['yaxis'+str((i+1))].update(showticklabels=False)

    #fig['layout']['xaxis'].update(title='Trading Week')
    #fig['layout']['yaxis'].update(title='Price (Cents)')
    fig['layout']['xaxis'].update(showticklabels=False)
    #fig['layout']['yaxis'].update(ticks='')
    cf.iplot(fig)
    

    