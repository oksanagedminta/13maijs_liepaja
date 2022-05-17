"""
linspace (sākums, beigas, num, beigu punkts = True, retstep = False,
 dtype = None , axis = 0 ) 
linespace - atgriezt vienādi izvietotus skaitļus noteiktā intervālā.

Izveidot sin funkcijas grafiku ar sākumu 0, beigās -200, bet skaitļu skaits 100.

linspace ir iekš numpy
"""
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0, 50, 100)
y=np.sin(x)

plt.plot(x, y)

plt.xticks(rotation="vertical") # x ass ciparus pagriežam
plt.show()