import pandas
import numpy
from collections import namedtuple

def get_data():
    # Load and process the training data
    print('Loading and preprocessing training data...')
    path = '../data/data.csv'
    df = preprocess_data(path)
    return df

def preprocess_data(path):
    df = pandas.read_csv(path, header=0)
    df = df.drop('Name', axis=1)
    df ['Operator'] = df['Operator'].apply(map_operator)
    df.Time = df.Time.apply(lambda time: numpy.clip(time,0,180))
    #df ['SumOperators'] = df.Operand1 + df.Operand2
    df ['big10Op1'] = df.Operand1.apply(lambda op :op > 10)
    df ['big10Op2'] = df.Operand2.apply(lambda op :op > 10)
    df ['big50Op1'] = df.Operand1.apply(lambda op :op > 50)
    df ['big50Op2'] = df.Operand2.apply(lambda op :op > 50)
    return df

def map_operator(op):
    switcher = {
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4,
    }
    return switcher.get(op,0)
