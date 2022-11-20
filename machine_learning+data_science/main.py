# Machine learning 101:
# 1 - Import the data
# 2 - Clean the data
# 3 - Split data. Training Set/Test Set
# 4 - Create a Model
# 5 - Check the output
# 6 - Improve
import pandas as pd

data_frame = pd.read_csv("data.csv")


print(data_frame["club"].head())

