import re
from datetime import datetime
import os

output=str(datetime.today())[0:10]
os.system('mkdir '+output)

def combo(host, email):
    with open(output+'/'+host+'.txt', "a+") as separa:
        separa.seek(0)
        linha=separa.read(50)
        if len(linha) > 0:
            separa.write("\n")
        separa.write(email)

db=open(input('Caminho da DB: '), 'r').read().splitlines()
print('Separando combos, aguarde...')
for email in db:
    host=re.search('@(.*):', email).group(1)
    combo(host, email)
    
print("Combos separados!")
    
