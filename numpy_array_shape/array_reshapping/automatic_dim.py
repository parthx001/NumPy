import numpy as np
arr=np.array([2,5,4,6,7,9])
arr1=arr.reshape(3,-1)
arr2=arr.reshape(-1,3)
print(arr)
print(arr1)
print(arr2)