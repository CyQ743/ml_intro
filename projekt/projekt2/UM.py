import os
import pickle
import logging
import pandas as pd
from sklearn.preprocessing import (StandardScaler, OrdinalEncoder, OneHotEncoder)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


X_train = pd.read_pickle('../../data/X_train.pkl')
    y_train = pd.read_pickle('../../data/y_train.pkl')
    X_test = pd.read_pickle('../../data/X_test.pkl')
    y_test = pd.read_pickle('../../data/y_test.pkl')

