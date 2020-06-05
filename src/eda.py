import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

def EDA(data,address)
	"""This function accepts a pandas dataframe and outputs histograms corresponding to the target variable (0,1)"""
        for feat in features.columns:
	    fig, ax = plt.subplots(figsize=(12, 8))
            ax.hist([features[target == 0][feat].values, features[target == 1][feat].values])
            ax.set_xlabel(' '.join(feat.split('_')).capitalize())
            ax.set_ylabel('Number of observations')
	    fig.savefig(address + feat +".png")
