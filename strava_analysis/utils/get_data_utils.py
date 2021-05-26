import pandas as pd 
import requests
import sys
import urllib3





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
    
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    # print(my_dataset)
    print(my_dataset[0]["name"])
    # print(my_dataset[0]["map"]["summary_polyline"])

    return my_dataset
