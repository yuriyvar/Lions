"""
This module is created to load data from the box office mojo files
"""

# imports
import os
import json

#constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')
MC_DIR = os.path.join(DATA_DIR, 'metacritic')


def load_mojo_data():
    """
    This function takes a json and outputs a dict!
    """
    file_list = os.listdir(MOJO_DIR)
    dict_list = []
    for fname in file_list:
        filepath = os.path.join(MOJO_DIR, fname)
        with open(filepath, 'r') as f:
            movie = json.load(f)
        dict_list.append(movie)
    return dict_list

def load_mc_data():
    """
    This function takes a json and outputs a dict!
    """
    file_list = os.listdir(MC_DIR)
    dict_list = []
    for fname in file_list:
        filepath = os.path.join(MC_DIR, fname)
        with open(filepath, 'r') as f:
            movie = json.load(f)
        dict_list.append(movie)
    return dict_list
    
def to_df(list_dict):
    '''
    This function is specifically designed to pull the MetaCritic set
    into a DF, by removing the list columns in the dictionary list
    '''
    import pandas as pd
    list_list = ['num_critic_reviews', 'num_user_reviews', 'genre']
#    test_col = list_dict[0]
#    for i in test_col.keys():
#        if type(y[i])==list:
#            list_list.append(i)
    new_list = []
    for mdict in list_dict:
        if len(mdict)==15:        
            for col in list_list:
                mdict.pop(col)
            new_list.append(mdict)
    df = pd.DataFrame(new_list)
    return df
        
        
        
