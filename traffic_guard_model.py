# imported modules
import pandas as pd
#import numpy as np
import stumpy


# import data


# preprocess data


# feature engineering


# modelling
def get_similarity_score(ip):
    if ip:
        # TODO: mock
        if ip == '0.0.0.0' or ip == '256.256.256.256':
            return 0.9
        else:
            return 0.6
    else:
        print("Error: IP value cannot be empty")
        return -1
