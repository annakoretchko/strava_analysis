import os
import sys

import get_data.get_data as get_data
import analyze_data.analyze_data as analyze_data
#import strava_analysis.get_data.get_data as get_data
#import strava_analysis.analyze_data.analyze_data as analyze_data


def main():

    if sys.platform == "linux" or sys.platform == "linux2":
        # linux
        # define pre-existing variables
        os.environ['historic_activities_raw'] =r'/Users/anna/Google Drive/Projects/strava_analysis/strava_analysis/data/historic_activities_raw.csv'
    elif sys.platform == "darwin":
        # OS X
        # define pre-existing variables
        os.environ['historic_activities_raw'] =r'/Users/anna/Google Drive/Projects/strava_analysis/strava_analysis/data/historic_activities_raw.csv'
    elif sys.platform == "win32":
        # Windows...
            # define pre-existing variables
        os.environ['historic_activities_raw'] =r'C:\Users\annab\Google Drive\Projects\strava_analysis\strava_analysis\data\historic_activities_raw.csv'


  
    # # # gets the strava data via api requests and save to csv
    get_data.run()

    # analyzes the data from strava
    analyze_data.run()
    





if __name__ == '__main__':
    main()