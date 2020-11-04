import re, os
from datetime import datetime
os.system('mkdir /sdcard/ComboSuit')

def sepdom(host, combo):
    with open(dir+host+'.txt', "a+") as sep:
        sep.seek(0)
        lin=sep.read(150)
        if len(lin) > 1:
            sep.write("\n")
        sep.write(combo)

def change(combo):
    with open(txt, 'a+') as chan:
        chan.seek(0)
        line=chan.read(150)
        if len(line) > 1:
            chan.write("\n")
        chan.write(combo)
    
output=str(datetime.today())[0:10]

print('''Tools:
1 > separar combos por dominio (gmail, hotmail, yahoo...)
2 > Trocar separador : para |.
3 > Trocar separador | para :.
''')

tool=input('Selecione a tool (1,2 ou 3): ')

db=open(input('Caminho da DB: '), 'r').read().splitlines()

if tool=='1':
    dir='/sdcard/ComboSuit/'+output+'-Host/'
    os.system('mkdir '+dir)
    for combo in db:
        host=re.search('@(.*):', combo).group(1)
        sepdom(host, combo)
elif tool=='2':
    dir='/sdcard/ComboSuit/'+output+'-Separador'
    txt=dir+'/Out-'+str(datetime.now())[11:19]+'.txt'
    os.system('mkdir '+dir)
    for combo in db:
        combo=combo.replace('|', ':')
        change(combo)
elif tool=='3':
    dir='/sdcard/ComboSuit/'+output+'-Separador'
    txt=dir+'/Out-'+str(datetime.now())[11:19]+'.txt'
    os.system('mkdir '+dir)
    for combo in db:
        combo=combo.replace(':', '|')
        change(combo)
else:
    print('a tool selecionada e invalida')
    exit('tool invalida')
print('Tarefa realizada!')
