from preprocessing import get_data
from training import train
from benchmark import benchmark

df = get_data()
benchmark(df)
#train (df)
