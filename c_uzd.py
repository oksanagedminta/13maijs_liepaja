"""
Nolasīt faila c_uzd.txt, kā 2dimensiju masīvu.
No datiem izveidot apļa diagrammu, izmantojot 
noformējuma piemēru - c_uzd.png.
"""
import matplotlib.pyplot as plt
import numpy as np
# 2 no faila mums vajag datus sadalīt 2 masīvos
names=[]
work=[]


# 1
for line in open("c_uzd.txt", "r"):
    data=[i for i in line.split()]
    names.append(data[0])
    new_data=[j for j in data[1].split("%")]
    work.append(new_data[0])
colors=["yellow", "b", "g", "cyan", "red"]

plt.pie(work, labels=names, colors=colors, startangle=90,
        shadow=True, radius=1.2, autopct="%1.1f%%")
plt.show()
