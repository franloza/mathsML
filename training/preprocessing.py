import pandas
import numpy
from collections import namedtuple

def get_data():
    # Load and process the training data
    print('Loading and preprocessing training data...')
    path = '../data/data.csv'
    values = preprocess_data(path)

    # Split features and label
    data, target = values[:,:-1], values[:,-1:]
    dataset = namedtuple('Dataset', ['data', 'target'])
    dataset.data = data
    dataset.target = target.ravel()

    return dataset

def preprocess_data(path):
	df = pandas.read_csv(path, header=0)

	df = df.drop('Name', axis=1)
	df.Time = df.Time.apply(lambda time: numpy.clip(time,0,180))

	return df
