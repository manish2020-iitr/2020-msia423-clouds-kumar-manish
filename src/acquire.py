import logging
import pandas as pd
import requests
import numpy as np

logger = logging.getLogger(__name__)

def acquire(url, column_names = None, first_cloud_row_beg = 53, first_cloud_row_end = 1077, second_cloud_row_beg = 1082, second_cloud_row_end = 2105):
   
    """
    This function aquires data from asource url and returns a pandas dataframe
    Input : 1. url (string)
        2. Index of the begining record for first cloud (int)
	3. Index of the begining record of second cloud (int)
	4. Index of last record for first cloud (int)
	5. Index of last record of second cloud (int)
    Output : A pandas datafrme 
    """
    logger.info("Acquiring data from %s", url)
    response = requests.get(url)

    text_first_cloud_data = (response.text).splitlines()[first_cloud_row_beg:first_cloud_row_end]
    first_cloud = [[s for s in line.split(' ') if s != ''] for line in text_first_cloud_data]
    first_cloud_df = pd.DataFrame(first_cloud, columns=column_names)
    first_cloud_df['class'] = np.zeros(first_cloud_df.shape[0])

    text_second_cloud_data = (response.text).splitlines()[second_cloud_row_beg:second_cloud_row_end]
    second_cloud = [[s for s in line.split(' ') if s != ''] for line in text_second_cloud_data]
    second_cloud_df = pd.DataFrame(second_cloud, columns=column_names)
    second_cloud_df['class'] = np.ones(second_cloud_df.shape[0])

    df = first_cloud_df.append(second_cloud_df)

    return df
