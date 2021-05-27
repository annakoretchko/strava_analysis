import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime as date
import os
import sys

import strava_analysis.utils.general_utils as general_utils


def speed_vs_distance(file_path):
    """[Investigates to see if there is a relationship between 
        how far I run and my average speed]
    """
    
    # reads in activities df
    df = pd.read_csv(file_path)


    #Create new dataframe with only columns I care about
    cols = ['name', 'activity_id', 'type', 'distance', 'moving_time',   
            'average_speed', 'max_speed','total_elevation_gain',
            'start_date_local'
        ]
    df = df[cols]



    #Break date into start time and date
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['start_time'] = df['start_date_local'].dt.time
    df['start_date_local'] = df['start_date_local'].dt.date

    # select only runs (although tbh, it's already nearly just that)
    runs = df.loc[df['type'] == 'Run']

    # create graph to investigate avg speed vs distance
    sns.set(style="ticks", context="talk")
    sns.regplot(x='distance', y = 'average_speed', data = runs).set_title("Average Speed vs Distance")
    # saves image
    general_utils.save_image(plt,"avg_speed_vs_distance")

    # create graph to investigate max speed vs distance
    sns.scatterplot(x='distance', y = 'max_speed', data = runs).set_title("Max Speed vs Distance")
    # saves image
    general_utils.save_image(plt,"max_speed_vs_distance")


def max_speed_over_time(file_path):
    """[Plots the maxed speed over time.]
    """
    # reads in activities df
    df = pd.read_csv(file_path)

    print(df['start_date_local'].head())
    print(df['start_date_local'].tail())
    sys.exit()
    #Create new dataframe with only columns I care about
    cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',   
            'average_speed', 'max_speed','total_elevation_gain',
            'start_date_local'
        ]
    df = df[cols]


    #Break date into start time and date
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['start_time'] = df['start_date_local'].dt.time
    df['start_date_local'] = df['start_date_local'].dt.date

    # select only runs (although tbh, it's already nearly just that)
    runs = df.loc[df['type'] == 'Run']
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.asarray(runs.start_date_local)
    y = np.asarray(runs.max_speed)
    ax.plot_date(x, y)
    ax.set_title('Max Speed over Time')
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    # saves image
    general_utils.save_image(plt,"max_speed_over_time")
    


def avg_speed_over_time(file_path):
    """[Graphs average speed over time]
    """

    # reads in activities df
    df = pd.read_csv(file_path)


    #Create new dataframe with only columns I care about
    cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',   
            'average_speed', 'max_speed','total_elevation_gain',
            'start_date_local'
        ]
    df = df[cols]


    #Break date into start time and date
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['start_time'] = df['start_date_local'].dt.time
    df['start_date_local'] = df['start_date_local'].dt.date

    # select only runs (although tbh, it's already nearly just that)
    runs = df.loc[df['type'] == 'Run']

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    x = np.asarray(runs.start_date_local)
    y = np.asarray(runs.average_speed)
    ax1.plot_date(x, y)
    ax1.set_title('Average Speed over Time')
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    # saves image
    general_utils.save_image(plt,"avg_speed_over_time")



def compare_time_frames(file_path,start_1, end_1, start_2, end_2):
    """[Takes two sets of times periods and compares results of the two time frames]

    Args:
        file_path ([str]): [path to csv]
        start_1 ([type]): [beginning of time_frame_1]
        end_1 ([type]): [end of time_frame_1]
        start_2 ([type]): [beginning of time_frame_2]
        end_2 ([type]): [end of time_frame_2]
    """
    # Run faster in NC or SoFlo?

    # reads in activities df
    df = pd.read_csv(file_path)


    #Create new dataframe with only columns I care about
    cols = ['name', 'upload_id', 'type', 'distance', 'moving_time',   
            'average_speed', 'max_speed','total_elevation_gain',
            'start_date_local'
        ]
    df = df[cols]


    #Break date into start time and date
    df['start_date_local'] = pd.to_datetime(df['start_date_local'])
    df['start_time'] = df['start_date_local'].dt.time
    df['start_date_local'] = df['start_date_local'].dt.date
    
    run = df.loc[df['type'] == 'Run'] 
    #add home / dc classification 2020-06-27 is date switch
    # convert time strings
    #dc_date = date.strptime(dc_date, '%Y-%m-%d').date()
    start_1 = date.strptime(start_1, '%Y-%m-%d').date()
    end_1 = date.strptime(end_1, '%Y-%m-%d').date()
    start_2 = date.strptime(start_2, '%Y-%m-%d').date()
    end_2 = date.strptime(end_2, '%Y-%m-%d').date()

    run['start_date_local'] = pd.to_datetime(run['start_date_local']).dt.date

    # chunk time frames

    # create column that is T if in t1 and F all else
    run['time_frame_1'] = np.where( (run['start_date_local'] > start_1) & (run['start_date_local'] < end_1), 'T', 'F')
    # get rows that fall in t1 column 
    time_frame_1 = run.loc[run['time_frame_1'] == 'T']
    
    # create column that is F if in t2 and F all else
    run['time_frame_2'] = np.where( (run['start_date_local'] > start_2) & (run['start_date_local'] < end_2), 'T', 'F')
    # get rows that fall in t2 column
    time_frame_2 = run.loc[run['time_frame_2'] == 'T']

    # get speed for each time period and also converts (time is in seconds, distance is in meters.
    #  m/s to mph 1 m/s to 2.237 mph)
    t1_speed = round(time_frame_1['average_speed'].mean() * 2.237, 2)
    t2_speed = round(time_frame_2['average_speed'].mean() * 2.237, 2)
    t1_max_speed = round(time_frame_1['max_speed'].mean()* 2.237, 2)
    t2_max_speed = round(time_frame_2['max_speed'].mean()* 2.237, 2)
    print("Average T1 Speed: " + str(t1_speed) + " | Average T1 Max Speed: " + str(t1_max_speed) + '\n'
        + "Average T2 Speed: " + str(t2_speed) + " | Average T2 Max Speed: " + str(t2_max_speed))

    percent_increase_average = round((t2_speed - t1_speed) * 100 / t1_speed,2)
    print("Percent increase average speed:",percent_increase_average)

    percent_increase_average_max = round((t2_max_speed - t1_max_speed) * 100 / t1_max_speed,2)
    print("Percent increase max speed:",percent_increase_average_max)

    sns.scatterplot(x='total_elevation_gain', y = 'average_speed', data = run).set_title("Speed vs Elevation Gain")
    # saves image
    general_utils.save_image(plt,"speed_vs_elevation_gain")
