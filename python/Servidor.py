import socket
import sys
import threading

def Conexion(connection,client_address):
    try:
        while True:
            data = connection.recv(1024) #definir quantos bytes são recebidos
            if data:
                mensaje = data.decode()
                print("Dado recebido de",client_address, ": %s" % mensaje)
                respuesta="--Mensagem recebida--"
                connection.send(bytes(respuesta,"utf-8"))
                #Aqui você pode adicionar as respostas ou o que você quer fazer com os resultados recebidos
				
                if mensaje=="Saida":
                    connection.close()
    except:
        connection.close()

def Iniciar(ip,puerto):
    # Criando o soquete TCP / IP (protocolo de comunicação)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Soquete e link de porta
    server_address = (ip, puerto) #Você pode mudar o IP
    print('Abrindo IP %s na porta %s' % server_address)
    sock.bind(server_address)
    sock.listen(1)
    listaConexiones =[] #armazenar as conexões
    hilosConexiones=[] #armazenar os encadeamentos de conexão (escucha)
    while True:
        # Esperando conexao
        print ('Esperando conexao...')
        connection, client_address = sock.accept()

        try:
            print ('Novo cliente, conectado de', client_address)
            listaConexiones.append(connection)
            try:
                #Para cada cliente cria um
               t = threading.Thread(target=Conexion, args=(connection,client_address,))
               hilosConexiones.append(t)
               t.start()
            except:
               print ("Erro: o encadeamento não pôde ser iniciado") 
        except:
           sock.close()
           
Iniciar("localhost",8080)
