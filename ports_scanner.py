import nmap

nm = nmap.PortScanner()

modo = ''
range_portas = ''

while not any([modo=='1' or modo=='2' or modo=='3']):
    modo = input("Modo de Scanner, digite o número correspondente ao modo: \n1. Scannear um host específico\n2. Todos os hosts da rede\n3. Localhost\n")
    if not any([modo=='1' or modo=='2' or modo=='3']):
        print('----------------------------------------------------')
        print("digite no terminal '1', '2' ou '3' !!!!")
        

print('----------------------------------------------------')

if modo == '1':
    host = input("digite o ip do host a ser buscado: ")
    print('----------------------------------------------------')
    lista_hosts = [host]
elif modo == '2':
    lista_hosts = nm.all_hosts()
else:
    lista_hosts = ["127.0.0.1"]

while not any([range_portas=='1' or range_portas=='2']):
    range_portas = input("Range de portas tcp a serem scanneada, digite o número correspondente ao range de portas desejado: \n1. Digitar manualmente o range de portas\n2. Scannear todas as portas tcp\n")
    if not any([range_portas=='1' or range_portas=='2']):
        print('----------------------------------------------------')
        print("digite no terminal '1' ou '2' !!!!")
        

print('----------------------------------------------------')
if range_portas == '1':
    print("Digite o início e o fim do range de portas\n")
    inicio = input("Início: ")
    fim = input("Fim: ")
    lista_portas = inicio + '-' + fim
    print('----------------------------------------------------')

else:
    lista_portas = '0-65535'

print("aguarde um momento ... ")

for host in lista_hosts:
    nm.scan(host, lista_portas)

    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('Estado : %s' % nm[host].state())

    portas = nm[host]['tcp'].keys()

    print('----------------------------------------------------')
    for porta in portas:
        print ('porta : %s\testado : %s\tnome : %s' % (porta, nm[host]['tcp'][porta]['state'], nm[host]['tcp'][porta]['name']))
