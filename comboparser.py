import re, os
from datetime import datetime

workdir=os.path.join('/', 'sdcard', 'ComboSuitByPoisonBR')
if not os.path.exists(workdir):
    os.mkdir(workdir)
domdir=os.path.join('/', 'sdcard', 'ComboSuitByPoisonBR', 'PorDominio')
if not os.path.exists(domdir):
    os.mkdir(domdir)
sepdir=os.path.join('/', 'sdcard', 'ComboSuitByPoisonBR', 'Separador')
if not os.path.exists(sepdir):
    os.mkdir(sepdir)

def sepdom(host, combo):
    with open(dir+'/'+host+'.txt', "a+") as sep:
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

print('''Tools:
1 > separar combos por dominio (gmail, hotmail, yahoo...)
2 > Trocar separador : para |.
3 > Trocar separador | para :.
''')

tool=input('Selecione a tool (1,2 ou 3): ')

db=open(input('Caminho da DB: '), 'r').read().splitlines()

if tool=='1':
    dir=os.path.join('/', 'sdcard', 'ComboSuitByPoisonBR', 'PorDominio', str(datetime.today())[0:10])
    if not os.path.exists(dir):
        os.mkdir(dir)
    for combo in db:
        host=re.search('@(.*):', combo).group(1)
        sepdom(host, combo)
elif tool=='2':
    txt=sepdir+'/Out-'+str(datetime.now())[11:19]+'.txt'
    for combo in db:
        combo=combo.replace('|', ':')
        change(combo)
elif tool=='3':
    txt='sepdir+'/Out-'+str(datetime.now())[11:19]+'.txt'
    for combo in db:
        combo=combo.replace(':', '|')
        change(combo)
else:
    print('a tool selecionada e invalida')
    exit('tool invalida')

print('Tarefa realizada!')
