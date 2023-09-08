import numpy as np
x = np.random.normal( size=(1000000,5), loc=[20,30,20,50,30], scale=[5, 5, 5, 5, 5] )
print("Shape of data: ", x.shape )
print("First vector:  ", x[0])
