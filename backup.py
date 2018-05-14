import os
from datetime import date
import shutil
import teste

today = str (date.today())
print (today)

pastadestino = "/hdext/"
novapastadestino = input ('diretorio destino:')
if novapastadestino != "":
    pastadestino = novapastadestino

if  os.path.exists (pastadestino+today):
    print ("Pasta já existe")
else:
    os.makedirs (pastadestino+today)
    print ("Criando Pasta")
