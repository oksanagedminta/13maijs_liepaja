"""
Ierakstīt, noskrāpējot datus, texta failā f_uzd.txt visas profesijas, firmas,
 kuras tās piedāvā, kā arī firmu adreses. 
 Terminālī izdrukāt piedāvāto  profesiju skaitu.
 url - https://realpython.github.io/fake-jobs/
"""
import requests
from lxml import html
from bs4 import BeautifulSoup

url="https://realpython.github.io/fake-jobs/"
page=requests.get(url)
soup=BeautifulSoup(page.text, "html.parser")
results=soup.find(id="ResultsContainer")

elements=results.find_all("div", class_="card-content")

profesijas=results.find_all("h2", class_="title")
print(profesijas)   #terminālī izdrukas prof.

for elements in elements:
    profesija=elements.find("h2", class_="title")
    kompanija=elements.find("h3", class_="company")
    vieta=elements.find("p", class_="location")

    f=open("f_uzd.txt", "a")
    f.write(profesija.text.strip()+"\n")
    f.write(kompanija.text.strip()+"\n")
    f.write(vieta.text.strip()+"\n")
    f.write("\n")   #lai ir atstarpe starp vizītkartēm
    f.close
