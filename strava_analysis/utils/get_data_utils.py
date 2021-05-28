import pandas as pd 
import requests
import sys
import os
import urllib3

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


import strava_analysis.utils.general_utils as general_utils


def get_updated_access_token(refresh_token,client_id,client_secret):
    """[Strava API requires an access token which needs to be refreshed frequently. In 
    order to circumvent this, we use the static refresh token, to generate a new 
    access token each time more data is pulled. 
    
    Helpful video for how to do this: https://www.youtube.com/watch?v=sgscChKfGyg ]
    """
    
    # blocks error messages
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # link to go from refresh token --> access token (the later is needed to actually get the data)
    auth_url = "https://www.strava.com/oauth/token"


    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': "refresh_token",
        'f': 'json'
    }

    print("Requesting Token...\n")\

    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    print("Access Token = {}\n".format(access_token))

    return access_token



def get_activities(access_token):
    """[API call to get list of all activities and their information, converts
    JSON to df, saves df as csv in data folder]

    Args:
        access_token ([str]): [updated access token]

    """

    # api request to get activities
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()

    #convert json to pandas df
    df = pd.json_normalize(my_dataset)

    #save df to data folder as csv
    general_utils.save_data_csv(df, 'new_activities_raw')


    

    return df

  

def combine_new_and_old_data(path_new,path_historic):


    # rename unique ids for both 
    df_new = pd.read_csv(path_new)
    df_new = df_new.rename(columns = {"id" :"activity_id"})

    df_historic = pd.read_csv(path_historic)
    df_historic = df_historic.rename(columns = {"Activity ID" :"activity_id"})
    df_historic = df_historic.rename(columns = {"Activity Type" :"type"})
    df_historic = df_historic.rename(columns = {"Elevation Gain" :"total_elevation_gain"})


    # make all column headers lower case for each
    df_new = df_new.rename(columns=str.lower)
    df_historic = df_historic.rename(columns=str.lower)

    # remove spaces in columns headers for each
    df_new.columns = df_new.columns.str.replace(" ","_")
    df_historic.columns = df_historic.columns.str.replace(" ","_")
    df_historic["distance"] = df_historic["distance"].str.replace(",","") # historic data can be 1,223 as string needs to be float


    df_historic["distance"] = pd.to_numeric(df_historic["distance"])

    # some historic dont have avg speed not sure why but we have time and distance so we can create
    df_historic['average_speed'].fillna(df_historic['distance'] / df_historic['moving_time'], inplace=True)
    
    

    
    # convert historic and new data columns that need conversion
    # df_new['distance']  = df_new['distance'] .div(1000)
    # df_new['distance'] = df_new['distance'].round(decimals = 2)
    df_new["distance"] = (0.621371 * df_new["distance"])/1000

    df_new['average_speed'] = df_new['average_speed'].round(decimals = 1)
    df_historic['average_speed'] = df_historic['average_speed'].round(decimals = 1)

    df_new['max_speed'] = df_new['max_speed'].round(decimals = 1)
    df_historic['max_speed'] = df_historic['max_speed'].round(decimals = 1)

    df_new['average_cadence'] = df_new['average_cadence'].round(decimals = 1)
    df_historic['average_cadence'] = df_historic['average_cadence'].round(decimals = 1)

    df_new['average_watts'] = df_new['average_watts'].round(decimals = 1)
    df_historic['average_watts'] = df_historic['average_watts'].round(decimals = 1)

    # different time

    

    #Break date into start time and date
    df_new['start_date_local'] = pd.to_datetime(df_new['start_date_local'])
    df_new['start_time'] = df_new['start_date_local'].dt.time
    df_new['start_date_local'] = df_new['start_date_local'].dt.date
    # create new column to join with (this is the 'real' date)
    df_new['activity_date'] = df_new['start_date_local']

  
    # convert to match 
    df_historic['activity_date'] = pd.to_datetime(df_historic['activity_date'])
    df_historic['activity_date'] = df_historic['activity_date'].dt.date
 
    # concats the two dfs
    df_combo = pd.concat([df_new,df_historic])
    # drops any duplicates
    df_combo = df_combo.drop_duplicates(subset=['activity_id'])

 
    
    # saves
    general_utils.save_data_csv(df_combo, 'combined_activities')




def combine_new_and_old_data2(path_new,path_historic):

    df_strava_api = pd.read_csv(path_new)
    # rename unique ids for both 
    df_strava_api = pd.read_csv(path_new)
    df_strava_api = df_strava_api.rename(columns = {"id" :"activity_id"})

    df_strava_historic = pd.read_csv(path_historic)
    df_strava_historic = df_strava_historic.rename(columns = {"Activity ID" :"activity_id"})
    df_strava_historic = df_strava_historic.rename(columns = {"Activity Type" :"type"})


    ### clean new api data ###

    # create unique id to match new and old later
    df_strava_api = df_strava_api.rename(columns = {"id" :"activity_id"})
    # convert to miles
    df_strava_api["distance"] = ((0.621371 * df_strava_api["distance"])/1000).round(decimals = 2)
    df_strava_api['average_speed'] = df_strava_api['average_speed'].round(decimals = 3)
    df_strava_api['max_speed'] = df_strava_api['max_speed'].round(decimals = 3)
    df_strava_api['average_cadence'] = df_strava_api['average_cadence'].round(decimals = 1)
    df_strava_api['average_watts'] = df_strava_api['average_watts'].round(decimals = 1)
    #Break date into start time and date
    df_strava_api['start_date_local'] = pd.to_datetime(df_strava_api['start_date_local'])
    df_strava_api['start_time'] = df_strava_api['start_date_local'].dt.time
    df_strava_api['start_date_local'] = df_strava_api['start_date_local'].dt.date
    # create new column to join with (this is the 'real' date)
    df_strava_api['activity_date'] = df_strava_api['start_date_local']

    # renaming historic data columns
    df_strava_historic = df_strava_historic.rename(columns=str.lower)
    df_strava_historic.columns = df_strava_historic.columns.str.replace(" ","_")
    df_strava_historic["distance"] = df_strava_historic["distance"].str.replace(",","")

    # clean and convert historic data
    #df_strava_historic['distance'] = df_strava_historic['distance'].round(decimals = 3)
    df_strava_historic["distance"] = pd.to_numeric(df_strava_historic["distance"])
    df_strava_historic['average_speed'].fillna((df_strava_historic['distance'] / df_strava_historic['moving_time'])*1000, inplace=True)
    df_strava_historic["distance"] = (0.621371 * df_strava_historic["distance"]).round(decimals = 2) # convert to miles
    df_strava_historic['average_speed'] = df_strava_historic['average_speed'].round(decimals = 3)
    df_strava_historic['max_speed'] = df_strava_historic['max_speed'].round(decimals = 3)
    df_strava_historic['average_cadence'] = df_strava_historic['average_cadence'].round(decimals = 1)
    df_strava_historic['average_watts'] = df_strava_historic['average_watts'].round(decimals = 1)
    df_strava_historic['activity_date'] = pd.to_datetime(df_strava_historic['activity_date'])
    df_strava_historic['activity_date'] = df_strava_historic['activity_date'].dt.date

    # concats the two dfs
    df_combo = pd.concat([df_strava_api,df_strava_historic])
    # drop any overlaps (where API stuff overlaps with when I pulled the historic)
    df_combo = df_combo.drop_duplicates(subset=['activity_id'])

    # save the all cleaned data sources
    general_utils.save_data_csv(df_combo, 'combined_activities')
    general_utils.save_data_csv(df_strava_historic, 'historic_activities_clean')
    general_utils.save_data_csv(df_strava_api, 'new_activities_clean')




    