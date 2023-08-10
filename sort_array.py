# coding: utf-8
import array
def function(arr):
    for i in range(0,5):
        for j in range(0,4):
            if arr[j] > arr[j+1]:
                c = arr[j]
                arr[j] = arr[j+1] 
                arr[j+1] = c
    print(arr) 
    
arr2=array.array("i",[90,89,77,66,44]) 
function(arr2) 
