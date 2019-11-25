import numpy as np
import matplotlib.pyplot as plt

labes=['A','B','C','D']
fracs=[15,30,45,10]
explode=[0,0.1,0.05,0]

plt.axes(aspect=1)

plt.pie(x=fracs,labels=labes,autopct="%.0f%%",explode=explode,shadow=True)
plt.show()