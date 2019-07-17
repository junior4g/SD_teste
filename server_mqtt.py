#UFG-INF-Sistemas Distribuidos
#Cliente MQTT usando o paho - funciona como server
#Documentação: https://pypi.org/project/paho-mqtt/
#Versão: V001 - 09/06/2019 (somente para testes de comunicação)

#Packs
import sys
import paho.mqtt.client as mqtt
import time
from datetime import datetime

# -------- Configurações --------------	

# Definicão do broker (server). Opções online: test.mosquitto.org; iot.eclipse.org ou outro qualquer
broker_init = "test.mosquitto.org" #broker local -> mudar depois para o local certo (ip ou nome da máq. na aws)


#broker = input("Informe o broker, sugestão: 'test.mosquitto.org' ou ENTER  para localhost: ")
#if len(broker) < 1: broker = broker_init
broker = broker_init
#nclientname = input("Informe o número da catraca/porta de acesso: ")
nclientname = 'cliente'
clientname = nclientname + '-' + str(datetime.now()) 
# o datatime é só para não criar cliente com nomes iguais. "gamb" (arrumar uma forma mais elegante)
tpc_base = "catracas/#"
tpc = str(tpc_base)
#tpc = str(tpc_base + "/" + str(nclientname))
#registrando o nome do topico --- aqui será dinâmico configurado pelo usuário

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
	topic=msg.topic
	m_decode=str(msg.payload.decode("utf-8","ignore"))
	split_msg = m_decode.split('#') #separa campos
	#print(str(msg.topic) + "#", m_decode)
	print(split_msg[0]) #origem (tópico)
	print(split_msg[1]) #codigo do funcionario/ visitante
	print(split_msg[2]) #data-hora de acesso
	print("------")	

	#Inv function para verificar permissão (temporária)
	cod_user = split_msg[1]
	if cod_user in ('1','2','3','4','5','6','7','8','9','10'):
		client.publish(topic, split_msg[1] + " liberado")
	else:
		client.publish(topic, split_msg[1] + " acesso negado")

# instanciando o cliente. 
client = mqtt.Client (clientname) 
client.on_connect=on_connect
client.on_disconnet=on_disconnet
client.on_message=on_message
print("Conectado no broker", broker)

# conectar ao broker
client.connect(broker)

# se inscreve no tópico para receber reposta do server (via broker) 
client.subscribe(str(tpc))

# inicia loop
client.loop_start()	

# Tempo conexão ...
#parar loop
time.sleep(1000) 
client.loop_stop()
#desconetar cliente
client.disconnect()
