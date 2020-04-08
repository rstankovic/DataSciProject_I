import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

articleCode = 'pwn2-uj5i'
url = 'https://data.cdc.gov'
URLextend = f'/api/views/{articleCode}/rows.json?accessType=DOWNLOAD'
response = requests.get(url + URLextend).json()
print(response)