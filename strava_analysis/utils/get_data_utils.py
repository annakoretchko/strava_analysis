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
    general_utils.save_data_csv(df, 'new_activities')


    

    return df

  

def combine_new_and_old_data(path_new,path_historic):


    # rename unique ids for both 
    df_new = pd.read_csv(path_new)
    df_new = df_new.rename(columns = {"id" :"activity_id"})
    df_historic = pd.read_csv(path_historic)
    df_historic = df_historic.rename(columns = {"Activity ID" :"activity_id"})

    
    # make all column headers lower case for each
    df_new = df_new.rename(columns=str.lower)
    df_historic = df_historic.rename(columns=str.lower)

    # remove spaces in columns headers for each
    df_new.columns = df_new.columns.str.replace(" ","_")
    df_historic.columns = df_historic.columns.str.replace(" ","_")
    df_historic["distance"] = df_historic["distance"].str.replace(",","") # historic data can be 1,223 as string needs to be float



    # convert historic and new data columns that need conversion
    df_new['distance']  = df_new['distance'] .div(1000)
    df_new['distance'] = df_new['distance'].round(decimals = 2)

    df_new['average_speed'] = df_new['average_speed'].round(decimals = 1)
    df_historic['average_speed'] = df_historic['average_speed'].round(decimals = 1)

    df_new['max_speed'] = df_new['max_speed'].round(decimals = 1)
    df_historic['max_speed'] = df_historic['max_speed'].round(decimals = 1)

    df_new['average_cadence'] = df_new['average_cadence'].round(decimals = 1)
    df_historic['average_cadence'] = df_historic['average_cadence'].round(decimals = 1)

    df_new['average_watts'] = df_new['average_watts'].round(decimals = 1)
    df_historic['average_watts'] = df_historic['average_watts'].round(decimals = 1)

    
    

    # concats the two dfs
    df_combo = pd.concat([df_new,df_historic])
    # drops any duplicates
    df_combo = df_combo.drop_duplicates(subset=['activity_id'])

    df_combo["distance"] = pd.to_numeric(df_combo["distance"])
    
    # saves
    general_utils.save_data_csv(df_combo, 'combined_activities')



    