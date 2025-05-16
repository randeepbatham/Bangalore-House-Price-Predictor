import pickle
import json
import numpy as np


dataColumns = []
locations = []
model = None

def getLocationNames():
    return locations

def load_artifacts():
    global dataColumns, locations, model
    # Load columns
    with open("C:/Users/RANDEEP/My_Projects/ML_Projects/Bangalore-House-Price-Predictor/columns.json", 'r') as f:
        dataColumns = json.load(f)["data_columns"]
        locations = dataColumns[3:]

    # Load model
    with open("C:/Users/RANDEEP/My_Projects/ML_Projects/Bangalore-House-Price-Predictor/bangaloreHomePricesModel.pickle", 'rb') as f:
        model = pickle.load(f)

def getEstimatedPrice(location, sqft, bhk, bath):
    try:
        loc_index = dataColumns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(dataColumns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]