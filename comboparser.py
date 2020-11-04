import re, os, time

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
2 > Trocar separador | para : e vice-versa.
''')

try:
    tool=input('Selecione a tool (1 ou 2): ')

    db=open(input('Caminho da DB: '), 'rb').read().decode('utf-8',errors='ignore').splitlines()

    if tool=='1':
        dir=input('Digite um nome para a pasta de saida: ')
        dir=os.path.join('/', 'sdcard', 'ComboSuitByPoisonBR', 'PorDominio',dir)
        if not os.path.exists(dir):
            os.mkdir(dir)
        try:
            for combo in db:
                    host=re.search('@(.*):', combo).group(1)
                    sepdom(host, combo)
        except(AttributeError):
                    print('Voce deve trocar o separador antes (de | para :).'); time.sleep(3)
                    ex=input('Deseja trocar agora? (y/n): ')
                    if ex=='y' or ex=='Y' or ex=='yes' or ex=='Yes':
                            new=input('Defina o nome do novo arquivo: ')
                            txt=sepdir+'/'+new+'.txt'
                            for combo in db:
                                    combo=combo.replace('|', ':')
                                    change(combo)
                            db=open(txt, 'rb').read().decode('utf-8',errors='ignore').splitlines()
                            try:
                                    for combo in db:
                                            host=re.search('@(.*):', combo).group(1)
                                            sepdom(host, combo)
                            except:
                                    print('Tarefa realizada!')
                                    exit()
                    else:
                            print('Saindo...')
                            exit()
                    
    elif tool=='2':
        txt=input('Defina o nome do novo arquivo: ')
        txt=sepdir+'/'+txt+'.txt'
        for combo in db:
            try:
                    if re.search(':', combo).group()==':':
                            combo=combo.replace(':','|')
            except(AttributeError):
                    combo=combo.replace('|',':')
            change(combo)

    print('Tarefa realizada!')
except(KeyboardInterrupt):
    print('Cancelado pelo usuário.')
    exit('Ctrl-C pressionado')
