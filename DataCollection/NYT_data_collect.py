import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

def NYT_collect():
    directoryName = input('Please provide relative path of folder: ')
    statesOrCounties = input('would you like to grab the states or counties\
        data? (answer s or c) ')
    answerSC = False
    while not answerSC:
        if statesOrCounties == 's':
            statesOrCounties = 'states'
            answerSC = True
        elif statesOrCounties == 'c':
            statesOrCounties = 'counties'
            answerSC = True
        else:
            print('you did not enter "s" or "c"')
            statesOrCounties = input('would you like to grab the states or counties\
                data? (answer s or c)')
    file_path = f'{directoryName}/us-{statesOrCounties}.csv'
<<<<<<< HEAD
    #print(file_path)
    NYT_df = pd.read_csv(file_path)
    #print(NYT_df.head())
    saveFilePath = input('Please provide relative path to save .csv file to: ')+f'/NYT_{statesOrCounties}_data.csv'
    NYT_df.to_csv(saveFilePath)
    return saveFilePath
=======
    
    NYT_df = pd.read_csv(file_path)
    directoryName = input("please provide relative path of directory for .csv storage: ")
    NYT_df.to_csv(f'{directoryName}/NYT_{statesOrCounties}_data.csv')
>>>>>>> master
