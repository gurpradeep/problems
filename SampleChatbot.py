import json
import pickle
import random

import nltk
from nltk.stem import WordNetLemmatizer

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Activation, Dropout  