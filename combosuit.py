import re, os, time, datetime

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

os.system('git pull && clear')

print(f'''{C}
                            /+osyhhhhhhyys++/
                         +oydddhhhhyyhhhhdddhy+/
                      /+yddhyyyys.josue.syyhddhs/
                     +hddyyssssssssssssssssssyyhdds/
                   /sddhyyyyyyssssssssssssssyyyyyhmh+
                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo
                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo
                /hmmmy{B}.           `````          `{C}smddd+
                smddm/{B}     `````          `````   {C}mdhmh/
               +ddydm+{B}  -/osyyyys+.    ./syyyyso/-{C}mdydms
               ymhyhmh{B}.yyo/ -- +hdo  /dho -- /oyh.{C}ymdyymd/
              /dmyyymd{B}.  ``.-   ./   -/.-   .``  `{C}dmhsydmo
              smdysymd{B}   shdhyydy      sdyyhddy   {C}dmyyshmy
              dmysshmy{B}                            {C}smhssymd/
             /dmyssymd{B}                            {C}hmhsyymm/
             /dmyssyhms{B}                          /{C}mdysyymm/
             /dmyssyydm/{B}  sh       hh/     -hy  .{C}dmyssyymm/
              dmhssssydd/{B} -hdhysshdysdhssyhdd  -{C}hmhyssyymd/
              ymhssssyyddo{B}``. //+/.` ./+// -` /{C}ddhysssyhmh
              +mdysssssyhdh{B} `     `/+`      -{C}sddysssssydmo
               ymhysssssyyddh/{B}`   `dm.   ` {C}sddhysssssyhmh/
               /hmhysssssyyyhdds{B} ..dm . {C}ohddhyyssssyyhmd+
                /yddhyssssssyyhhddhddddddhyyssssssyydmh+
               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/
           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/
         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+
        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo
        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms
         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/
           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///
                       ///////+++++++++++++//////
     ██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗██████╗ ██████╗
     ██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
     ██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██████╔╝██████╔╝
     ██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██╔══██╗██╔══██╗
     ██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║
     ╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
     {RT}{B}*t.me/p0isonBR*{RT}'''); time.sleep(3)

os.system('clear')

print(f'''{B}*By PoisonBR
{G} █████╗ █████╗ ███╗   ███╗██████╗  █████╗ {C}██████╗██╗  ██╗██╗███████╗
{G}██╔═══╝██╔══██╗████╗ ████║██╔══██╗██╔══██╗{C}██╔═══╝██║  ██║██║╚═██╔══╝
{G}██║    ██║  ██║██╔████╔██║██████╔╝██║  ██║{C}██████╗██║  ██║██║  ██║   
{G}██║    ██║  ██║██║╚██╔╝██║██╔══██╗██║  ██║{C}╚═══██║██║  ██║██║  ██║   
{G}╚█████╗╚█████╔╝██║ ╚═╝ ██║██████╔╝╚█████╔╝{C}██████║╚█████╔╝██║  ██║   
 {G}╚════╝  ╚═══╝ ╚═╝     ╚═╝╚═════╝  ╚════╝ {C}╚═════╝ ╚════╝ ╚═╝  ╚═╝ {G}v1.0{C}
[{G}i{C}] Os arquivos de saida ficarão na pasta: /sdcard/ComboSuitByPoisonBR/
 ''')

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
	while True:
		with open(dir+'/'+host+'.txt', "a+") as sep:
			try:
				sep.seek(0)
				lin=sep.read(150)
				if len(lin) > 1:
					sep.write("\n")
				sep.write(combo)
				break
			except:
				break

def change(combo):
	with open(txt, 'a+') as chan:
		chan.seek(0)
		line=chan.read(150)
		if len(line) > 1:
			chan.write("\n")
		chan.write(combo)

print(f'''{C}Selecione o modo de operação:
{C}[{G}1{C}] {B}separar combos por dominio ({C}gmail.com{B}, {C}hotmail.com{B}, {C}globo.com{B}...)
{C}[{G}2{C}] {B}Trocar separador {C}| {B}para {C}: {B}e vice-versa.{C}
''')

try:
	tool=input(f'{C}Selecione ({G}1 {C}ou {G}2{C}): ')

	db=open(input(f'{C}[{G}+{C}] Caminho da DB: {B}'), 'rb').read().decode('utf-8',errors='ignore').splitlines()
	inicio=str(datetime.datetime.now())

	if tool=='1':
		dir=input(f'{C}[{G}*{C}] Digite um nome para a pasta de saida:{B} ')
		dir=os.path.join('/', 'sdcard', 'ComboSuitByPoisonBR', 'PorDominio',dir)
		if not os.path.exists(dir):
			os.mkdir(dir)
		print(G+str(len(db))+C+' combos no arquivo. operação iniciada as '+G+inicio[11:19])
		for combo in db:
			try:
				if ('@') in combo:
					combo=combo.strip()
					host=re.search('@(.*?):', combo).group(1)
					sepdom(host, combo)
				else:
					continue
			except(AttributeError):
				continue

	elif tool=='2':
		txt=input(f'{C}[{G}*{C}]Defina o nome do novo arquivo:{B} ')
		txt=sepdir+'/'+txt+'.txt'
		for combo in db:
			try:
				if re.search(':', combo).group()==':':
					combo=combo.replace(':','|')
			except(AttributeError):
				combo=combo.replace('|',':')
			change(combo)
	else:
		print(f'{C}[{R}-{C}] Forma de operação selecionada inválida.')
		exit()
	fim=str(datetime.datetime.now())
	print(f'{C}[{G}+{C}] {G}Operação finalizada as {C}'+fim[11:19]+G+'.'+C)
except(KeyboardInterrupt):
	print(f'{C}[{R}-{C}] Cancelado pelo usuário.')
	exit(f'{Y}Ctrl-C pressionado{C}')
except(FileNotFoundError):
	print(f'{C}[{R}-{C}] Arquivo ou diretorio não encontrado.')
