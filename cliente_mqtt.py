#UFG-INF-Sistemas Distribuidos
#Cliente MQTT usando o paho (porta de acesso - catraca)
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
tpc_base = "catracas"
print("--- CONFIGURAÇÕES DA CATRACA DE ACESSO --- ")
tpc_a = input("Informe o 'prédio ou recepcao' (P01, P02, ..., R01, R02): ")
tpc_b = input("Informe o andar (A00, A01, A02, ...: ")
tpc_c = input("Informe o nome da catraca de acesso (CAT01, CAT01, CAT02, ...: ")

tpc = str(tpc_base + "/" + str(tpc_a) + "/" + str(tpc_b) + "/" + str(tpc_c))
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
	print("["+str(msg.topic)+"]:",m_decode)


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
	msg_acess = input("Digite o código do usuário: ")
	data_e_hora_atuais = datetime.now()
	data_e_hora_str = data_e_hora_atuais.strftime('%Y/%m/%d %H:%M:%S')
	msg_acess_comp = str(tpc) + '#' + msg_acess + '#' + data_e_hora_str
	client.publish(tpc,str(msg_acess_comp)) 
	print("... enviado para fila (broker)")

# Tempo conexão ...
#para loop
#time.sleep(200) 
#client.loop_stop()
#desconetar cliente
#client.disconnect()
