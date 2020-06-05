import logging
import numpy as np

logger = logging.getLogger(__name__)

def featurize_visible_range(data):

    data['visible_range'] = (data.visible_max - data.visible_min)
    if (data['visible_range'] < 0).any():
        return None
    else:
        df = data
        return df

def featurize_vis_norm_range(data):
    if (data['visible_mean'] == 0).any():
        return None
    else:
        data['visible_norm_range'] = (data.visible_max - data.visible_min).divide(data.visible_mean)
        df = data
        return df

def featurize_log_entropy(data):
    if (data['visible_entropy'] == 0).any():
        return None
    else :
        data['log_entropy'] = data.visible_entropy.apply(np.log)
        df = data
        return df

def featurize_entropy_x_contrast(data):
    data['entropy_x_contrast'] = data.visible_contrast.multiply(data.visible_entropy)
    df = data
    return df

def featurize_IR_range(data):
    data['IR_range'] = data.IR_max - data.IR_min
    if (data['IR_range'] < 0).any():
        return None
    else:
        df = data
        return df

def featurize_IR_norm_range(data):
    if (data["IR_mean"] == 0).any():
        return None
    else:
        data['IR_norm_range'] = (data.IR_max - data.IR_min).divide(data.IR_mean)
        df = data
        return df
