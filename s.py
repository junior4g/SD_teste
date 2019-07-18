#Packs
import sys
import paho.mqtt.client as mqtt
import time
from datetime import datetime

import redis
conn = redis.Redis('localhost')

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

data_e_hora_atuais = datetime.now()
data_e_hora_str = data_e_hora_atuais.strftime('%H:%M:%S %d/%m/%Y')

# Definicão do broker (server). Opções online: test.mosquitto.org; iot.eclipse.org ou outro qualquer
# broker local -> mudar depois para o local certo (ip ou nome da máq. na aws)
# test.mosquitto.org
broker_init = "test.mosquitto.org"

# broker = input("Informe o broker, sugestão: 'test.mosquitto.org' ou ENTER  para localhost: ")
broker = broker_init

# nclientname = input("Informe o número da catraca/porta de acesso: ")
nclientname = 'cliente'
clientname = nclientname + '-' + str(datetime.now()) 

# o datatime é só para não criar cliente com nomes iguais. "gamb" (arrumar uma forma mais elegante)
tpc_base = "projetosd:teste"
tpc = str(tpc_base)
#tpc = str(tpc_base + "/" + str(nclientname))

# Falta tratar as excessões
def on_log(client, userdata, level, buf):
	print("log: "+buf)

def on_connect(client, userdata, flags, rc):
	if rc==0:		
		#print()
		rc = 0
	else:
		print ("falha de conexao, codigo = ",rc)

def on_disconnet (client, userdata, flags, rc=0):
	print("Desconectado, codigo"+str(rc))	

def on_message(client,userdata,msg):


	topic    = msg.topic
	m_decode = str(msg.payload.decode("utf-8","ignore"))
	
	print("Mensagem recebida: ",m_decode)
	print("Cliente: ",client)
	print("Topico: ", topic)

	data_e_hora_atuais = datetime.now()
	data_e_hora_str = data_e_hora_atuais.strftime('%H:%M:%S %d/%m/%Y')
	print("Horario: ", data_e_hora_str)

	##################### Inicio operações com Redis #######################
	operacao = int(m_decode[0])

	if operacao == 1:
		# Opção cadastrar politica de acesso

		operacao, id, politica, local_de_acesso, horario_inicio, horario_fim = m_decode.split('#')

		politica = {"id": id, "politica": politica, "local_de_acesso": local_de_acesso,
					"horario_de_inicio": horario_inicio, "horario_fim": horario_fim}
		conn.hmset("politica:" + id, politica)

		print("Comando para consulta no Redis: hgetall politica:" + id)

	elif operacao == 2:
		# Opção cadastrar usuarios

		operacao, id, matricula, tipo_de_acesso = m_decode.split('#')

		user = {"id": id, "matricula": matricula, "tipo_de_acesso": tipo_de_acesso}
		conn.hmset("user:" + id, user)

		print("Comando para consulta no Redis: hgetall user:" + id)

	elif operacao == 3:
		# Opção cadastrar acesso

		operacao, matricula, predio, andar, tipo_de_acesso = m_decode.split('#')

		acesso = {"matricula": matricula, "predio": predio, "andar": andar, "tipo_de_acesso": tipo_de_acesso}
		conn.hmset("acesso:" + matricula, acesso)

		print("Comando para consulta no Redis: hgetall acesso:" + matricula)

		#print("\n Operacao 3")

	elif operacao == 4:
		# Opção cadastrar prédios

		operacao, id, nome, numero_de_andares, capacidade_de_pessoas_por_andar = m_decode.split('#')

		predio = {"id": id, "nome": nome, "numero_de_andares": numero_de_andares,
				  "capacidade_de_pessoas_por_andar": capacidade_de_pessoas_por_andar}
		conn.hmset("predio:" + id, predio)

		print("Comando para consulta no Redis: hgetall predio:" + id)

	elif operacao == 5:
		print("Operacao 5 sendo foi executada")

	print("-------------------------------------------------------------------------------")

	##################### Final operações com Redis #######################

# instanciando o cliente. 
client = mqtt.Client (clientname) 
client.on_connect = on_connect
client.on_disconnet = on_disconnet
client.on_message = on_message
print("Conectado no broker", broker)
print("Horario: ", data_e_hora_str)

print("\n                             RECEBENDO MENSAGENS                             ")
print("-------------------------------------------------------------------------------")

# conectar ao broker
client.connect(broker)

# se inscreve no tópico para receber reposta do server (via broker) 
client.subscribe(str(tpc))

# inicia loop
client.loop_start()	

# Tempo conexão ...
# parar loop
time.sleep(1000) 
# client.loop_stop()
# desconetar cliente
# client.disconnect()