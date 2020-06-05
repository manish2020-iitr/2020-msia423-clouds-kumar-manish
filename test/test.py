from src.featurize import *
import pandas as pd
import pytest

inp_dict = {
    'visible_mean': [1,1,1,1],
    'visible_max': [200.0, 210.0, 180.0, 180.0],
    'visible_min': [100.0, 50.0, 90.0, 120.0],
    'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
    'visible_contrast': [700, 800, 800, 946],
    'visible_entropy': [1,1,1,1],
    'visible_second_angular_momentum': [2.5,4.82,4.21,3.9],
    'IR_mean': [160,123,158,167],
    'IR_max': [234,345,278,321],
    'IR_min': [180,150,140,190]
    }

input_df = pd.DataFrame(inp_dict)

def test_visible_range_happy():
    '''
    Checking if a temperory df is same as original df
    '''

    exp_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 1, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,123, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [180, 150, 140, 190],
        'visible_range': [100.0, 160.0, 90, 60]
    }

    exp_df = pd.DataFrame(exp_df)
    true=featurize_visible_range(input_df)
    assert isinstance(true, pd.DataFrame)
    assert exp_df.equals(true)

def test_visible_range_unhappy():
    '''Passing a larger value in visible_min to check if a datframe is generated or not
    '''
    wrong_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 190.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 1, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,123, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [180, 150, 140, 190],
    }

    wrong_df = pd.DataFrame(wrong_df)
    true = featurize_visible_range(wrong_df)
    assert not(isinstance(true, pd.DataFrame))


def test_visible_norm_range_happy():
    '''Checking if a temp df is generated or not'''
    exp_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 1, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,123, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [180, 150, 140, 190],
        'visible_range': [100.0, 160.0, 90, 60],
        'visible_norm_range': [100.0, 160.0, 90, 60]
    }

    exp_df = pd.DataFrame(exp_df)
    true=featurize_vis_norm_range(input_df)
    assert isinstance(true, pd.DataFrame)
    assert exp_df.equals(true)


def test_visible_norm_range_unhappy():
    '''Passing 0 for one of the means and checking if a dataframe is generated
    '''
    wrong_df = {
        'visible_mean': [0,1,1,1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1,1,1,1],
        'visible_second_angular_momentum': [2.5,4.82,4.21,3.9],
        'IR_mean': [160,123,158,167],
        'IR_max': [234,345,278,321],
        'IR_min': [180,150,140,190]
    }

    wrong_df = pd.DataFrame(wrong_df)
    true = featurize_vis_norm_range(wrong_df)
    assert not(isinstance(true, pd.DataFrame))

def test_log_entropy_happy():
    '''Testing to see if a datframe with lof_entropy column is generated or not
    '''



    exp_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 1, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,123, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [180, 150, 140, 190],
        'visible_range': [100.0, 160.0, 90, 60],
        'visible_norm_range': [100.0, 160.0, 90, 60],
        'log_entropy': [0.0, 0.0, 0.0, 0.0]
    }
    exp_df = pd.DataFrame(exp_df)
    true=featurize_log_entropy(input_df)

    assert isinstance(true, pd.DataFrame)
    assert exp_df.equals(true)



def test_log_entropy_unhappy():
    '''Passing 0 for one of the values in visible_entropy
    '''
    wrong_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 0, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,123, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [180, 150, 140, 190],
        'visible_range': [100.0, 160.0, 90, 60],
        'visible_norm_range': [100.0, 160.0, 90, 60]
    }

    wrong_df = pd.DataFrame(wrong_df)
    true = featurize_log_entropy(wrong_df)
    assert not(isinstance(true, pd.DataFrame))





'''
def test_IR_range_happy():
    Checking to see if a dataframe is generated
  

    exp_df = {
        'visible_mean': [1,1,1,1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1,1,1,1],
        'visible_second_angular_momentum': [2.5,4.82,4.21,3.9],
        'IR_mean': [160,123,158,167],
        'IR_max': [234,345,278,321],
        'IR_min': [180,150,140,190],
        'IR_range': [54,195,138,131]
    }

    exp_df = pd.DataFrame(exp_df)
    true=featurize_IR_range(input_df)
    assert isinstance(true, pd.DataFrame)
    assert exp_df.equals(true)

'''

def test_IR_range_unhappy():
    '''Passing a larger value in IR_min than IR_max
    '''
    wrong_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 1, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,123, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [375, 150, 140, 190],
        'visible_range': [100.0, 160.0, 90, 60],
        'visible_norm_range': [100.0, 160.0, 90, 60]
    }

    wrong_df = pd.DataFrame(wrong_df)
    true = featurize_IR_range(wrong_df)
    assert not(isinstance(true, pd.DataFrame))


def test_IR_norm_range_unhappy():
    '''Passing a value of 0 for IR_mean
    '''
    wrong_df = {
        'visible_mean': [1, 1, 1, 1],
        'visible_max': [200.0, 210.0, 180.0, 180.0],
        'visible_min': [100.0, 50.0, 90.0, 120.0],
        'visible_mean_distribution': [0.05, 0.05, 0.09, 0.06],
        'visible_contrast': [700, 800, 800, 946],
        'visible_entropy': [1, 1, 1, 1],
        'visible_second_angular_momentum': [2.5, 4.82, 4.21, 3.9],
        'IR_mean': [160,0, 158, 167],
        'IR_max': [234, 345, 278, 321],
        'IR_min': [375, 150, 140, 190],
        'visible_range': [100.0, 160.0, 90, 60],
        'visible_norm_range': [100.0, 160.0, 90, 60]
    }

    wrong_df = pd.DataFrame(wrong_df)
    true = featurize_IR_norm_range(wrong_df)
    assert not(isinstance(true, pd.DataFrame))
