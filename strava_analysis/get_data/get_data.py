import pandas as pd 
import requests
import sys
import urllib3
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime as date
import os

from matplotlib.dates import *
import strava_analysis.utils.get_data_utils as get_data_utils
import secrets

def run():

    print('\nStart get_data initiated '+ str(date.now())+"\n")

    # first API call to get updated_access_token 
    updated_access_token = get_data_utils.get_updated_access_token(secrets.refresh_token, 
                                                                   secrets.client_id, 
                                                                   secrets.client_secret)

    # get activities and saves as csv in data folder
    df = get_data_utils.get_activities(updated_access_token)


    
    # adds new api activities data to historic already obtained data
    get_data_utils.combine_new_and_old_data(os.environ['new_activities_raw'],
                                            os.environ['historic_activities_raw'])


    print('Start get_data completed', date.now())




