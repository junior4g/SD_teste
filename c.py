#Packs
import sys
import paho.mqtt.client as mqtt
import time
from datetime import datetime

#Limpar tela
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#broker local -> mudar depois para o local certo (ip ou nome da máq. na aws)
#broker_init = "test.mosquitto.org"
broker_init = "test.mosquitto.org"

#broker = input("Informe o broker, sugestão: 'test.mosquitto.org' ou ENTER  para localhost: ")
#if len(broker) < 1: broker = broker_init
broker = broker_init

#nclientname = input("Informe o número da catraca/porta de acesso: ")
nclientname = 'cliente'
clientname = nclientname + '-' + str(datetime.now()) 

# o datatime é só para não criar cliente com nomes iguais. "gamb" (arrumar uma forma mais elegante)
#registrando o nome do topico --- aqui será dinâmico configurado pelo usuário
tpc = str("projetosd:teste")

# Falta tratar as excessões
def on_log(client, userdata, level, buf):
	print("log: "+buf)

def on_connect(client, userdata, flags, rc):
	if rc==0:		
		print("")
	else:
		print ("falha de conexao, codigo = ",rc)

def on_disconnet (client, userdata, flags, rc=0):
	print("Desconectado, codigo"+str(rc))	

def on_message(client,userdata,msg):
	topic    = msg.topic
	m_decode = str(msg.payload.decode("utf-8","ignore"))
	
	#print(str(msg.topic)+" : ",m_decode)


# instanciando o cliente. 
client = mqtt.Client (clientname) 
client.on_connect=on_connect
client.on_disconnet=on_disconnet

#client.on_log=on_log #ativar recebimento de logs
client.on_message=on_message  #ativar recebimento de mensagem / inclui a própria mensagem (tratar isso)
print("Conectado no broker", broker)

# conectar ao broker
client.connect(broker)

# se inscreve no tópico para receber reposta do server (via broker) 
client.subscribe(str(tpc))

# inicia loop
client.loop_start()	

# Entrada de dados (acesso) --> modularizar depois, usar loop e sleep
print("Aguardando entrada de dados ....")
print("--------------------------------")

cnt = 1

while(cnt > 0):
		#msg_acess = input("parada: ")
		#client.publish(tpc,str(input("Digite a mensagem: ")))

		# tcp.send (msg.encode('utf-8'))
		# msg = input()
		cls()
		print("\n\n")
		print("                     CONTROLE DE ACESSO DE CONDOMINIO                          ")
		print("                      GERENCIAMENTO - PAGINA INICIAL                           ")
		print("\n")
		print(" ##############################################################################")
		print(" |                                                                            |")
		print(" |   Digite um comando para prosseguir:                                       |")
		print(" |   1 - Cadastrar politica de acesso                                         |")
		print(" |   2 - Cadastrar usuarios                                                   |")
		print(" |   3 - Cadastrar acesso                                                     |")
		print(" |   4 - Cadastrar predios                                                    |")
		print(" |   5 - Teste de envio de mensagem                                           |")
		print(" |                                                                            |")
		print(" ##############################################################################")
		men = input("  Digite a opcao escolhida: ")

		men_int = int(men)  # Convertendo a mensagem em um inteiro

		if men_int == 1:
			cls()
			print("\n\n")
			print("                        CADASTRAR POLITICA DE ACESSO                           ")
			print("\n")
			print(" ##############################################################################")
			print(" |                                                                            |")
			print(" |   Voce deve informar a que usuario a politica de acesso se destina.        |")
			print(" |   - Funcionario                                                            |")
			print(" |   - Visitante                                                              |")
			print(" |   - Prestador de servico                                                   |")
			print(" |                                                                            |")
			print(" ##############################################################################")
			id = input(" ID: ")
			politica = input(" Tipo de usuario: ")
			local_de_acesso = input(" Local de acesso: ")
			horario_inicio = input(" Horario de inicio: ")
			horario_fim = input(" Horario final: ")

			men = "1#" + id + "#" + politica + "#" + local_de_acesso + "#" + horario_inicio + "#" + horario_fim

			client.publish(tpc, str(men))
			#tcp.send(men.encode('utf-8'))
			# sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

		elif men_int == 2:

			cls()
			print("\n\n")
			print("                              CADASTRAR USUARIOS                               ")
			print("\n")
			print(" ##############################################################################")
			print(" |                                                                            |")
			print(" |   Tipos de usuario                                                         |")
			print(" |   - Funcionario                                                            |")
			print(" |   - Visitante                                                              |")
			print(" |   - Prestador de servico                                                   |")
			print(" |                                                                            |")
			print(" ##############################################################################")
			id = input(" ID: ")
			matricula = input(" Matricula: ")
			tipo_de_acesso = input(" Tipo de acesso: ")

			men = "2#" + id + "#" + matricula + "#" + tipo_de_acesso

			client.publish(tpc, str(men))
			#tcp.send(men.encode('utf-8'))
			# sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

		elif men_int == 3:

			cls()
			print("\n\n")
			print("                              CADASTRAR ACESSO                                 ")
			print("\n")
			print(" ##############################################################################")
			print(" |                                                                            |")
			print(" |   Cadastrar acesso dos usuarios                                            |")
			print(" |                                                                            |")
			print(" |   Opcoes:                                                                  |")
			print(" |                                                                            |")
			print(" |   Predio 01                                                                |")
			print(" |   - 12 andares                                                             |")
			print(" |                                                                            |")
			print(" |   Predio 02                                                                |")
			print(" |   - 12 andares                                                             |")
			print(" |                                                                            |")
			print(" ##############################################################################")
			matricula = input(" Matricula: ")
			predio = input(" Predio: ")
			andar = input(" Andar: ")
			tipo_de_acesso = input(" Tipo de acesso: ")

			men = "3#" + matricula + "#" + predio + "#" + andar + "#" + tipo_de_acesso

			#operacao, matricula, predio, andar, tipo_de_acesso

			client.publish(tpc, str(men))
			#tcp.send(men.encode('utf-8'))
			# sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

		elif men_int == 4:

			cls()
			print("\n\n")
			print("                              CADASTRAR PREDIOS                                ")
			print("\n")
			print(" ##############################################################################")
			print(" |                                                                            |")
			print(" |   Cadastrar predios no condominio                                          |")
			print(" |                                                                            |")
			print(" |   Informe os dados solicitados                                             |")
			print(" |                                                                            |")
			print(" ##############################################################################")
			id = input(" ID: ")
			nome = input(" Nome: ")
			numero_de_andares = input(" Numero de andares: ")
			capacidade_de_pessoas_por_andar = input(" Capacidade de pessoas por andar: ")

			men = "4#" + id + "#" + nome + "#" + numero_de_andares + "#" + capacidade_de_pessoas_por_andar

			client.publish(tpc, str(men))
			#tcp.send(men.encode('utf-8'))
			# sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

		elif men_int == 5:
			client.publish(tpc, str("5#123#P01#CAT00#A03"))
			#tcp.send(men.encode('utf-8'))
			# sock.send(bytes(str(men_int), "utf-8"))  # Envia mensagem para o servidor

		else:
			print("Nao existe esta opcao, tente novamente!", "\n")


# Tempo conexão ...
#para loop
#time.sleep(200) 
#client.loop_stop()
#desconetar cliente
#client.disconnect()