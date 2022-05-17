"""
Izveidot apļveida diagrammu ar datiem par firmām Pankūkas, Biete, 
Bumbieris, Kartupelis, kuru dalība
projektā attiecīgi ir 35, 25, 25 un 15 mēneši.

Diagrammā izcelt Pankūkas un Kartupeļus, kā piemēru skatīt d_uzd.png.
"""
import matplotlib.pyplot as plt
import numpy as np


y=np.array([35, 25, 25, 15])
#print(y)   #pārbaudām
mylabels=["Pankūkas", "Biete", "Bumbieris", "Kartupelis"]
aka=[0, 0.2, 0, 0.2]    # lai izceļ no apļa

plt.pie(y, labels=mylabels, shadow=True, explode=aka)
plt.show()