import cv2 as cv   
import numpy as np  
import matplotlib.pyplot as plt 
y=np.array([23,44,56,32])
mylabe=["apple", "banana" , "mango" , "cherry"]
myexplod=[-0.5 , 0.3 , 0 ,0]
plt.pie(y,labels=mylabe , explode=myexplod , shadow=True)
plt.show()
