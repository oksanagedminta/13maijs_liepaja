"""
Attēlot datus, kuri saglabāti piem.txt failā, stabiņveida diagrammā.
Noformējuma piemērs - a_uzd.png.
"""
import matplotlib.pyplot as plt

# 2 no faila mums vajag datus sadalīt 2 masīvos
vardi=[]
marks=[]

# 1
f=open("piem.txt", "r")     #nosaucam = atveram("ko atveram", "kādā rež.")
# 3
for rinda in f: # no mūsu faila "f", katra rinda
    rinda=rinda.split(" ")  #norādām kā sadalīt texstu no faila (ar atstarpi)
    vardi.append(rinda[0])  # 0 pozīcijā ir vārds
    marks.append(int(rinda[1])) # 1 poz.ir skaitlis (int) - vecims

# 4 pārbaudam vai dati no faila ņemas
#print(vardi)
#print(marks)

# 5 zīmējam diagrammu
plt.bar(vardi, marks, color="g", label="no datnes")
plt.title("Sadalījums pēc vecuma")
plt.xlabel("Skolēna vārds", fontsize=12)
plt.ylabel("Vecums", fontsize=12)

plt.legend()    #funkcija, kura parāda uz diagrammas to ko esam norādījuši plt.bar=label
plt.show()

"""
xdati=["Dace", "Anna", "Beate", "Mareks", "Zigis"]
vecums=[12, 45, 22, 65, 25]

xpoint=np.array(vecums)

x=np.arange(len(xdati))

width=0.35  #stabiņu platums ko jāsadala uz 2:
fig, ax=plt.subplots()  #apakštabiņi

z=ax.bar(x-width/2, vecums, width, label="Vecums") 
ax.set_title("Sadalījums pēc vecuma")
ax.set_xlabel("skolēna vārds")


plt.show()
"""