#endereço Ethernet   IPv4 10.1.70.28
#endereço Ethernet 2 IPv4 192.168.56.1
#endereço Ethernet 3 IPv4 169.254.250.216

N = 83
G = 41
X = 8697

R1 = 0
R2 = 0

shift = 1

def cript(decriptedValue):
    criptedValue = ''

    for char in decriptedValue:
        criptedValue += chr(ord(char) + shift)
    
    return criptedValue

def decript(decriptedValue):
    criptedValue = ''

    for char in decriptedValue:
        criptedValue += chr(ord(char) - shift)
    
    return criptedValue

def getR1():
    return (G ** X) % N

def getK():
    return (R2 ** X) % N

from socket import *

R1 = getR1()

print('Valor de R1: ', R1)

serverName = "10.1.70.36"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Envio do R1 para o servidor
clientSocket.send(bytes(str(R1),"utf-8"))

# Recebimento do R2
R2 = int(clientSocket.recv(1024))

# Calculo do K (shift)
shift = getK()

# Valor do K (shift)
print('Valor do K (Shift): ' + str(shift))

sentence = input("Entrada para o servidor (decriptografada)): ")

sentence = cript(sentence)

print('Entrada para o servidor (criptografada): ' + sentence)

clientSocket.send(bytes(sentence, "utf-8"))

modifiedSentence = clientSocket.recv(1024)

text = str(modifiedSentence,"utf-8")

print('Recebido do servidor (criptografado): ', text)

print ('Recebido do servidor (decriptografado): ', decript(text))

clientSocket.close()
