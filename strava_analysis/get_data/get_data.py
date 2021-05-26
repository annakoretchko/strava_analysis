import pandas as pd 
import requests
import sys
import urllib3

import strava_analysis.utils.get_data_utils as get_data_utils
import secrets

def run():

    
    # first API call to get updated_access_token 
    updated_access_token = get_data_utils.get_updated_access_token(secrets.refresh_token, 
                                                                   secrets.client_id, 
                                                                   secrets.client_secret)

    # get activities
    activities = get_data_utils.get_activities(updated_access_token)



