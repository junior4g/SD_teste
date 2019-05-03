import socket
import sys
import threading

#Função para escutar o servidor
def Escuchar(servidor):
    try:
         while True:
            data = servidor.recv(1024) #se define cuantos bytes se reciben
            if data:
                mensaje=data.decode()
                #print("Dado recebido: %s" % mensaje,"\n")
    except:
        servidor.close()

def ConectarServidor(ip,puerto):
    # Criando um socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecte o soquete à porta quando o servidor estiver escutando
    server_address = (ip, puerto)
    print ('Conectando ao IP %s  %s' % server_address)
    sock.connect(server_address)

    try:
        hiloServidor = threading.Thread(target = Escuchar, args=(sock,))
        hiloServidor.start()
    except:
               print ("Erro: o encadeamento não pôde ser iniciado")

    #Enviando dados
    try:
        while True:
            men = input("Mensagem: ")
            sock.send(bytes(men,"utf-8"))
    except:
        print ('Conexao perdida, fechando o socket')
        sock.close()
        
ConectarServidor("localhost",8080)
