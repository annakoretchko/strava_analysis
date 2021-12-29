import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime as date
import os
import sys


import utils.analyze_data_utils as analyze_data_utils
import utils.general_utils as general_utils

# import strava_analysis.utils.analyze_data_utils as analyze_data_utils
# import strava_analysis.utils.general_utils as general_utils


def run():

    # investigates relationship between speed and distance
    analyze_data_utils.speed_vs_distance(os.environ['combined_activities'])

    # investigates max speed over time
    analyze_data_utils.max_speed_over_time(os.environ['combined_activities'])

    # investigates avg speed over time
    analyze_data_utils.avg_speed_over_time(os.environ['combined_activities'])

    # compares two time frames data
    analyze_data_utils.compare_time_frames(os.environ['combined_activities'],
                                           start_1 = '2019-07-01',
                                           end_1 = '2020-04-01', 
                                           start_2 = '2020-10-03', 
                                           end_2 = '2021-04-26')

    # investigating kudo 
    analyze_data_utils.kudo_analysis(os.environ['new_activities_clean'])







