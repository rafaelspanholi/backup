import os
from datetime import date
import shutil
import config

today = str (date.today())
print (today)

pastadestino = "f:/"
novapastadestino = input ('diretorio destino:')
if novapastadestino != "":
    pastadestino = novapastadestino

if  os.path.exists (pastadestino+today):
    print ("Pasta já existe")
else:
    os.makedirs (pastadestino+today)
    print ("Pasta Criada")

pasta1 = ("/dados")
def copiarpasta (origem,pastadestino):
    for arquivo in os.listdir (pasta1):
        s = os.path.join(pasta1, arquivo)
        d = os.path.join(pastadestino+today, arquivo)
        if os.path.isdir(s):
            shutil.copytree(s, d) 
        else:
            shutil.copy2(s, d)
pasta2 = ("/dados2")
copiarpasta (pasta1, pastadestino)
