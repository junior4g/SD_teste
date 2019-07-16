import socket

#Limpar tela
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

HOST = '52.90.38.46'     # Endereco IP do Servidor
PORT = 8000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print ('Para sair use CTRL+X\n')

msg = '\17'

while (msg != '\x18'):
        #tcp.send (msg.encode('utf-8'))
        #msg = input()
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
        print(" |   5 - Sair                                                                 |")
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

            tcp.send(men.encode('utf-8'))
            #sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

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

            tcp.send(men.encode('utf-8'))
            #sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

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

            tcp.send(men.encode('utf-8'))
            #sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

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

            tcp.send(men.encode('utf-8'))
            #sock.send(bytes(str(men), "utf-8"))  # Envia mensagem para o servidor

        elif men_int == 5:
            tcp.send(men.encode('utf-8'))
            #sock.send(bytes(str(men_int), "utf-8"))  # Envia mensagem para o servidor

        else:
            print("Nao existe esta opcao, tente novamente!", "\n")

tcp.close()