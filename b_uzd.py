""" Nolasīt faila datini.csv numpy, kā 2dimensiju masīvu.
No datiem izveidot līnijsveida diagrammu, izmantojot 
noformējuma piemēru - datini.png. """
import matplotlib.pyplot as pp
import numpy as np

# 1 nolasu failu iekš numpy kā divdimensiju masīvu
dati=np.loadtxt(fname="datini.csv", delimiter=";")

# 2 kā sadalīt divos lielumos x un y. Izveidojam duvus tukšus masīvus:
x=[]
y=[]

for i in range(len(dati)):
    for j in range(2):      # jo 2 elementi, kas ir 0 pozīcijā un 1 pozīcijā
        if j==0:
            x.append(dati[i][j])
        else:
            y.append(dati[i][j])
# 1.1.pārbaudām
#print(dati)
# 2.1 pārbaudām
#print(x)
#print(y)

# 3 tālāk veidojam diagrammu
pp.plot(x, y, label="Dati no faila")
pp.xlabel("x ass apzīmējums")
pp.ylabel("y ass apzīmējums")
pp.title("Lielais virsraksts")
pp.legend()
pp.show()