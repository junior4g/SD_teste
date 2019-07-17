#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import thread
import sys
import redis
conn = redis.Redis('localhost')

HOST = '192.168.1.107' # Endereco IP do Servidor
PORT = 8000            # Porta que o Servidor esta

def conectado(con, cliente):
    print ('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg)

        ##################### Inicio operações com Redis #######################
        operacao = int(mensagem[0])

        if operacao == 1:
            # Opção cadastrar politica de acesso

            operacao, id, politica, local_de_acesso, horario_inicio, horario_fim = mensagem.split('#')

            politica = {"id": id, "politica": politica, "local_de_acesso": local_de_acesso,
                        "horario_de_inicio": horario_inicio, "horario_fim": horario_fim}
            conn.hmset("politica:" + id, politica)

        elif operacao == 2:
            # Opção cadastrar usuarios

            operacao, id, matricula, tipo_de_acesso = mensagem.split('#')

            user = {"id": id, "matricula": matricula, "tipo_de_acesso": tipo_de_acesso}
            conn.hmset("user:" + id, user)

        elif operacao == 3:
            # Opção cadastrar acesso

            operacao, matricula, predio, andar, tipo_de_acesso = mensagem.split('#')

            acesso = {"matricula": matricula, "predio": predio, "andar": andar, "tipo_de_acesso": tipo_de_acesso}
            conn.hmset("acesso:" + matricula, acesso)

        elif operacao == 4:
            # Opção cadastrar prédios

            operacao, id, nome, numero_de_andares, capacidade_de_pessoas_por_andar = mensagem.split('#')

            predio = {"id": id, "nome": nome, "numero_de_andares": numero_de_andares,
                      "capacidade_de_pessoas_por_andar": capacidade_de_pessoas_por_andar}
            conn.hmset("predio:" + id, predio)

        ##################### Final operações com Redis #######################

    print ('Finalizando conexao do cliente', cliente)
    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()