#save df to output folder

import sys
import os
import pandas
import matplotlib.pyplot as plt



def save_data_csv(df,filename):

    """[Takes df and file name and saves it to data folder 
    (or creates data folder if it's not there, then saves).
    Also saves path as env variable for reference later if needed]
    """

    #save df to data folder
    cwd = os.getcwd()
    path_inside = os.path.join(cwd,'strava_analysis')
    output_path = os.path.join(path_inside,'data')

    # Create if data folder DNE
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    filename_csv = str(filename) + ".csv"
    file_out_path = os.path.join(output_path,filename_csv)

    # save df as csv
    df.to_csv(file_out_path,index = False)

    # path as environment variable
    os.environ[str(filename)] = file_out_path

def save_image(fig,filename,show = False):

    """[This takes fig and saves it to data folder (or creates
    data folder if it's not there, then saves)]
    """
    if show:
        plt.show()
    #save df to data folder
    cwd = os.getcwd()
    path_inside = os.path.join(cwd,'strava_analysis')
    output_path = os.path.join(path_inside,'data')

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # saves image to output folder
    filename_img = str(filename) + ".png"

    pout = os.path.join(output_path,filename_img)
    plt.savefig(pout)
    plt.close()


    

    