import re, os
from datetime import datetime

def sepdom(host, combo):
    with open('/sdcard/ComboSuit/'+output+'-Host'+'/'+host+'.txt', "a+") as sep:
        sep.seek(0)
        lin=sep.read(50)
        if len(lin) > 0:
            sep.write("\n")
        sep.write(combo)

def change(combo):
    with open('/sdcard/ComboSuit/'+output+'-Separador'+'/Out-'+str(datetime.now())[11:19]+'.txt', 'a+') as chan:
        chan.seek(0)
        line=chan.read(50)
        if len(line) > 0:
            chan.write("\n")
        chan.write(combo)
    
output=str(datetime.today())[0:10]
char={'|' :':', ':' :'|'}

print('''Tools:
1 > Trocar separador | para : e vice-versa.
2 > separar combos por dominio (gmail, hotmail...).
''')

tool=input('Selecione a tool (1 ou 2): ')

db=open(input('Caminho da DB: '), 'r').read().splitlines()

if tool=='1':
    os.system('cat > /sdcard/'+output+'-Separador'+'/Out-'+str(datetime.now())[11:19]+'.txt')
    for combo in db:
        for key,value in char.items():
            combo=combo.replace(key,value)
            change(combo)
elif tool=='2':
    os.system('cat > /sdcard/ComboSuit/'+output+'-Host'+'/'+host+'.txt')
    for combo in db:
        host=re.search('@(.*):', combo).group(1)
        sepdom(host, combo)
else:
    print('a tool selecionada e invalida')
    exit('tool invalida')
print('Tarefa realizada!')
