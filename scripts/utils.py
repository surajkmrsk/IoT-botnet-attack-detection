import pandas as pd
import os
from glob import glob


# This function will read all the bengin data and load into bengin dataframe.
def load_device_data(PATH, EXT):
    """
    Creates a data frame consisting of all the .csv-files in a given directory. The directory should
    be where the unzipped data files are stored. Assumes the file structurce is
        device name
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    PATH : str
        The directory in which the data files are stored. 
    EXT : str
        Extension of the file
        
    Returns
    -------
    benign_data : pandas data frame 
        consisting of all the bengin data.
            
    """
    benign_dfs = []
    mirai_dfs = []
    gafgyt_dfs = []
    for path, subdir, files in os.walk(PATH):
        for file in glob(os.path.join(path, EXT)):
            if 'benign_traffic' in file:
                data = pd.read_csv(file)
                data['label'] = 'Benign'
                data['device'] = file.split('\\')[1]
                benign_dfs.append(data)
            if 'mirai_attacks' in file:
                data = pd.read_csv(file)
                data['label'] = 'Mirai'
                data['device'] = file.split('\\')[1]
                mirai_dfs.append(data)
            if 'gafgyt_attacks' in file:
                data = pd.read_csv(file)
                data['label'] = 'Gafgyt'
                data['device'] = file.split('\\')[1]
                gafgyt_dfs.append(data)

    benign_data = pd.concat(benign_dfs, ignore_index=True)
    mirai_data = pd.concat(mirai_dfs, ignore_index=True)
    gafgyt_data = pd.concat(gafgyt_dfs, ignore_index=True)

    return benign_data, mirai_data, gafgyt_data