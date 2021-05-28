import os

import strava_analysis.get_data.get_data as get_data
import strava_analysis.analyze_data.analyze_data as analyze_data


def main():

    # define pre-existing variables
    os.environ['historic_activities_raw'] =r'/Users/anna/Google Drive/Projects/strava_analysis/strava_analysis/data/historic_activities_raw.csv'
    # # os.environ['combined_activities'] = r'/Users/anna/Google Drive/Projects/strava_analysis/strava_analysis/data/combined_activities.csv'
    # # os.environ['new_activities'] = r'/Users/anna/Google Drive/Projects/strava_analysis/strava_analysis/data/new_activities.csv'
    # # # gets the strava data via api requests and save to csv
    get_data.run()

    # analyzes the data from strava
    analyze_data.run()
    





if __name__ == '__main__':
    main()