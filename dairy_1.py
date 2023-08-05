# coding: utf-8
# coding: utf-8
import pandas as pd 
import statistics as scs 
data=pd.read_csv("dairy_dataset.csv") 
data 
print(data.head())
print(" \n")
print(" \n")
print(data.loc[4] )
print(" \n")
print(" \n")
data.columns 
data.info() 
data.isnull() 
data.isnull().loc[4] 
data.isnull()
data.isnull().loc[2000] 
data.loc[2000] 
data[["Location","Product Name","Price per Unit"]] 
Unique_Location = data[["Location"]].value_counts() 
print(" \n")
print(" \n")
print(" \n")
print(Unique_Location) 
print(" \n")
print(" \n")
print(" \n")
Delhi_farm=data[data["Location"]=="Delhi"] 
print(Delhi_farm )
print(Delhi_farm.head() )
print(" \n")
print(" \n")
print(" \n")
print(Delhi_farm.loc[31] )
print(" \n")
print(" \n")
print(" \n")
print(" \n")
improved_data=data[["Location","Product Name","Brand","Price per Unit","Total Value","Shelf Life (days)","Storage Condition"]] 
improved_data 
print(improved_data.loc[4] )
print(" \n") 
improved_data.describe 
improved_data.describe() 
#improved_data.groupby(["Product Name"]).sum() 
groupby_product=improved_data.groupby(["Product Name"]).sum()
#print(groupby_product.plot.bar())
import matplotlib.pyplot as plt
    
