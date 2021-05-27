import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime as date
import os
import sys

import strava_analysis.utils.analyze_data_utils as analyze_data_utils
import strava_analysis.utils.general_utils as general_utils


def run():

    # investigates relationship between speed and distance
    analyze_data_utils.speed_vs_distance(os.environ['combined_activities'])

    # investigates max speed over time
    analyze_data_utils.max_speed_over_time(os.environ['combined_activities'])

    # investigates avg speed over time
    analyze_data_utils.avg_speed_over_time(os.environ['combined_activities'])

    # compares two time frames data
    analyze_data_utils.compare_time_frames(os.environ['combined_activities'],
                                           start_1 = '2020-06-27',
                                           end_1 = '2020-10-27', 
                                           start_2 = '2020-10-28', 
                                           end_2 = '2021-02-26')






