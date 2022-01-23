import sklearn.preprocessing as preprocessing
import numpy as np
import pandas as pd

targets = np.array(["Sun", "Sun", "Moon", "Earth", "Monn", "Venus"])
labelenc = preprocessing.LabelEncoder()
labelenc.fit(targets)
targets_trans = labelenc.transform(targets)
print("The original data")
print(targets)
print("The transform data using LabelEncoder")
print(targets_trans)