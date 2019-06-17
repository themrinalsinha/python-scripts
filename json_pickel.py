import pickle
import numpy as np

data_dict = {
    'volts': np.random.random(10000),
    'current': np.random.random(10000),
}

# Writing data to pickle file
with open('data_pickel.pkl', 'wb') as pickle_file:
    pickle.dump(data_dict, pickle_file)

# Reading data from pickle file
with open('data_pickel.pkl', 'rb') as pickle_file:
    data_dict = pickle.load(pickle_file)
    print(data_dict)
