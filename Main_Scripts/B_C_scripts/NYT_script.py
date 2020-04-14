import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
#from NYT_data_collect import saveFilePath


file_path = '../../Resources/NYT_counties_data.csv'
NYT_df = pd.read_csv(file_path)
file_path = '../../Resources/UnemploymentUSA.csv'
unemployment_df = pd.read_csv(file_path)
print(NYT_df.head())
print()
print(unemployment_df.head())

# plt.figure(figsize=(10,10))
# plt.pie(NYT_df.groupby(["state"])["cases"].count(),autopct='%1.1f%%')
# plt.show()