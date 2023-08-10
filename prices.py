# coding: utf-8
import pandas as pd
import numpy as np 
price=pd.read_excel("Price.xlsx") 
price
price.describe()
price.Price.mean() 
price.Price.median() 
price.Price.std() 
