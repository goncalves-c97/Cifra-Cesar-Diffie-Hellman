from socket import *

#Métodos de criptografia e decriptografia

N = 83
G = 41
Y = 6732458

def calcR2():
    return (G ** Y) % N     

shift = 1

def encript(decriptedValue):
    criptedValue = ''

    for char in decriptedValue:
        criptedValue += chr(ord(char) + shift)
    
    return criptedValue

def decript(decriptedValue):
    criptedValue = ''

    for char in decriptedValue:
        criptedValue += chr(ord(chr(char)) - shift)
    
    print(type(criptedValue))
    return criptedValue

R2 = calcR2()
print("R2 " + str(R2))
serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()
r1 = int(connectionSocket.recv(65000))
connectionSocket.send(bytes(str(R2), "utf-8"))
shift = (r1 ** Y) % N
print(shift)

sentence = connectionSocket.recv(65000)

received = str(sentence,"utf-8")

print (received , " texto recebido encriptado") #Encripto

received = decript (sentence)

print (received , " texto decriptado") #Cripto

print ("Received From Client: ", received)

capitalizedSentence = received.upper() # processamento

capitalizedSentence = encript (capitalizedSentence)

print (capitalizedSentence , " encriptando novamente para enviar") #Cripto

encodedCapitalizedSentence = capitalizedSentence.encode()
connectionSocket.send(encodedCapitalizedSentence)


sent = str(encodedCapitalizedSentence,"utf-8")
print ("Sent back to Client: ", sent)
connectionSocket.close()
