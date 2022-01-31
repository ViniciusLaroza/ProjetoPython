class Piloto():
    def __init__(self):
        self.registroPiloto = 0
        self.nomePiloto = ''
        self.nascimentoPiloto = ''
        self.qtddVoo = 0.0
        self.emailPiloto = ''
        self.telefonePiloto = ''

ListaPilotos = []

class Voo():
    def __init__(self):
        self.numeroVoo1 = 0
        self.cidadeOrigem = ''
        self.cidadeDestino = ''
        self.tempoMedio = 0.0
        self.aeronave = ''
        self.cidadesEscala = []

listaVoo = []

class Viagem():
    def __init__(self):
        self.numeroVoo = 0
        self.piloto = ''
        self.data = ''
        self.hora = ''
        self.qtddPassageiros = 0

listaViagem = []


def arqExiste(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

print(arqExiste('pilotos.txt'))
print(arqExiste('voo.txt'))
print(arqExiste('viagem.txt'))

#-------------------------------------Cadastro-----------------------------------------#

def cadastrarPiloto():
    p = Piloto()
    p.registroPiloto = input('Digite o registro do piloto:(1234567890...) ')
    existe = verificandoRegistroRepetido(p.registroPiloto, ListaPilotos)
    if existe == True:
        print('Nao é possivel cadastrar/registro do piloto ja cadastrado.')
    else:
        p.nomePiloto = input('digite o nome do piloto: ')
        dataValida = False
        while not dataValida:
            p.nascimentoPiloto = input('nascimento do piloto: (dd/mm/aaaa) ')
            dataDia = int(p.nascimentoPiloto[0:2])
            dataMes = int(p.nascimentoPiloto[3:5])
            semLetra = any(char.isalpha() for char in p.nascimentoPiloto)
            if p.nascimentoPiloto[2] == '/' and p.nascimentoPiloto[5] == '/' and (
                    int(dataDia) < 32 and 13 > dataMes) and not semLetra:
                dataValida = True
            else:
                print('Data inválida. Digite novamente.')
        p.qtddVoo = float(input('digite o tempo total de horas de voo: '))
        p.emailPiloto = input('digite o email do piloto: ')
        p.telefonePiloto = input('digite o telefone do piloto: ')
        ListaPilotos.append(p)

def cadastrarVoo():
    v = Voo()
    v.numeroVoo1 = input('digite o numero do voo: ')
    existe = verificandoVooRepetido(v.numeroVoo1, listaVoo)
    if existe == True:
        print('Nao é possivel cadastrar/numero do voo ja cadastrado.')
    else:
        v.cidadeOrigem = input('digite a cidade de origem: ')
        v.cidadeDestino = input('digite a cidade de destino: ')
        v.tempoMedio = float(input('digite o tempo medio do voo:(ex -> 13.30) '))
        v.aeronave = input('digite o nome da aeronave: ')
        cidadesEscala = ''
        while cidadesEscala != 'fim':
            cidadesEscala = input('digite as cidades da escala e fim para terminar: ')
            if cidadesEscala != 'fim':
                v.cidadesEscala.append(cidadesEscala)
        listaVoo.append(v)

def cadastrarViagem():
    g = Viagem()
    g.numeroVoo = input('digite o numero do voo:')
    existe2 = verificandoNumVooRepetido(g.numeroVoo, listaViagem)
    if existe2 == True:
        print('Nao é possivel cadastrar/numero de voo ja cadastrado.')
    else:
        existe = False
        for elemento in listaVoo:
            if elemento.numeroVoo1 == g.numeroVoo:
                existe = True
        if not existe:
            print('Voo nao cadastrado.')
        else:
            g.piloto = input('digite o nome do piloto: ')
            existe1 = verificandoRegistroPiloto2Repetido(g.piloto, listaViagem)
            if existe1 == True:
                print('Nao é possivel cadastrar/piloto ja selecionado.')
            else:
                existe = False
                for elemento in ListaPilotos:
                    if elemento.nomePiloto == g.piloto:
                        existe = True
                if not existe:
                    print('Piloto não cadastrado.')
                else:
                    g.data = input('digite a data:(d/m/yyyy) ')
                    existe3 = verificandoDataRepetida(g.data, listaViagem)
                    if existe3 == True:
                        print('Nao é possivel cadastrar/data ja cadastrada, recomeçe o cadastro.')
                    else:
                        g.hora = input('digite a hora do voo:(ex 13H30)')
                        existe4 = verificandoHoraRepetida(g.hora, listaViagem)
                        if existe4 == True:
                            print('Não é possivel cadastrar/hora ja cadastrada, recomeçe o cadastro.')
                        else:
                            g.qtddPassageiros = int(input('digite a quantidade de passageiros: '))
                            listaViagem.append(g)

#----------------------------------------------LISTAGEM----------------------------------------------------------------#

def listarTodosPilotos():
    cont = 0
    for elemento in ListaPilotos:
        cont = cont + 1
        print('Cadastro do piloto', cont)
        print('--'*30)
        print('registro piloto',[cont],':',elemento.registroPiloto)
        print('nome piloto',[cont],':',elemento.nomePiloto)
        print('data de nascimento',[cont],':',elemento.nascimentoPiloto)
        print('horas de voo',[cont],':',elemento.qtddVoo)
        print('email',[cont],':',elemento.emailPiloto)
        print('telefone',[cont],':',elemento.telefonePiloto)
        print('--'*30)

def listarTodosVoos():
    cont = 0
    for elemento in listaVoo:
        cont = cont+1
        print('Cadastro do voo', cont)
        print('--' * 30)
        print('Numero do voo',[cont],':',elemento.numeroVoo1)
        print('Cidade origem',[cont],':',elemento.cidadeOrigem)
        print('Cidade destino',[cont],':',elemento.cidadeDestino)
        print('Tempo medio da viagem',[cont],':',elemento.tempoMedio)
        print('Nome da aeronave',[cont],':',elemento.aeronave)
        print('Cidades escala', [cont],':',elemento.cidadesEscala)
        print('--'*30)

def listarTodasViagens():
    cont = 0
    for elemento in listaViagem:
        cont = cont + 1
        print('Cadastro da viagem', cont)
        print('--' * 30)
        print('Numero do voo', [cont], ':', elemento.numeroVoo)
        print('Piloto', [cont], ':', elemento.piloto)
        print('Data da partida', [cont], ':', elemento.data)
        print('Hora da partida', [cont], ':', elemento.hora)
        print('Quantidade de passageiros', [cont], ':', elemento.qtddPassageiros)
        print('--' * 30)

def listarElementoEspecificoPiloto():
    print('1-Registro Pilotos')
    print('2-Nome Pilotos')
    print('3-Datas de nascimento')
    print('4-Horas de voo ')
    print('5-Email')
    print('6-Telefones')
    pergunta = input('digite o que deseja listar: ')
    cont = 0
    for elemento in ListaPilotos:
        cont = cont + 1
        if pergunta == '1':
            print('registro do piloto', [cont], ':', elemento.registroPiloto)
        if pergunta == '2':
            print('nome piloto', [cont], ':', elemento.nomePiloto)
        if pergunta == '3':
            print('data de nascimento', [cont], ':', elemento.nascimentoPiloto)
        if pergunta == '4':
            print('horas de voo', [cont], ':', elemento.qtddVoo)
        if pergunta == '5':
            print('email', [cont], ':', elemento.emailPiloto)
        if pergunta == '6':
            print('telefone do piloto', [cont], ':', elemento.telefonePiloto)

def listarElementoEspecificoViagem():
    print('1-Numero do voo')
    print('2-Piloto')
    print('3-Data da partida')
    print('4-Hora da partida')
    print('5-Quantidade de passageiros')
    pergunta = input('digite o que deseja listar: ')
    cont = 0
    for elemento in listaViagem:
        cont = cont + 1
        if pergunta == '1':
            print('numero do voo',[cont],':',elemento.numeroVoo)
        if pergunta == '2':
            print('Piloto',[cont],':',elemento.piloto)
        if pergunta == '3':
            print('Data da partida',[cont],':',elemento.data)
        if pergunta == '4':
            print('Hora da partida',[cont],':',elemento.hora)
        if pergunta == '5':
            print('Quantidade de passageiros',[cont],':',elemento.qtddPassageiros)

def listarElementoEspecificoVoo():
    print('1-Numero do voo')
    print('2-Cidade Origem')
    print('3-Cidade destino')
    print('4-Tempo medio da viagem')
    print('5-Nome da aeronave')
    print('6-Cidades escala')
    pergunta = input('digite o que deseja listar: ')
    cont = 0
    for elemento in listaVoo:
        cont = cont +1
        if pergunta == '1':
            print('numero do voo',[cont],':',elemento.numeroVoo1)
        if pergunta == '2':
            print('cidade origem',[cont],':',elemento.cidadeOrigem)
        if pergunta == '3':
            print('cidade destino',[cont],':',elemento.cidadeDestino)
        if pergunta == '4':
            print('tempo medio da viagem',[cont],':',elemento.tempoMedio)
        if pergunta == '5':
            print('nome da aeronave',[cont],':',elemento.aeronave)
        if pergunta == '6':
            print('Cidades escala', [cont], ':',elemento.cidadesEscala)

#-------------------------------------------VERIFICACAO-----------------------------------------------------------------

def verificandoRegistroPiloto2Repetido(registro, listaViagem):
    for elemento in listaViagem:
        if elemento.piloto == registro:
            return True
    return False

def verificandoNumVooRepetido(num, listaViagem):
    for elemento in listaViagem:
        if elemento.numeroVoo == num:
            return True
    return False

def verificandoDataRepetida(dat, listaViagem):
    for elemento in listaViagem:
        if elemento.data == dat:
            return True
    return False

def verificandoHoraRepetida(hr, listaViagem):
    for elemento in listaViagem:
        if elemento.hora == hr:
            return True
    return False

def verificandoVooRepetido(numVoo, listaVoo):
    for elemento in listaVoo:
        if elemento.numeroVoo1 == numVoo:
            return True
    return False

def verificandoRegistroRepetido(registro, ListaPilotos):
    for elemento in ListaPilotos:
        if elemento.registroPiloto == registro:
            return True
    return False

#--------------------------------------------------RELATORIO------------------------------------------------------------
from datetime import *


def RelatorioPiloto():
    digiteQtddVoo = input('Digite a quantidade minima de horas de voo dos pilotos que deseja mostrar: ')
    cont = 0
    for elemento in ListaPilotos:
        cont = cont + 1
        if float(elemento.qtddVoo) >= float(digiteQtddVoo):
            print('--' * 30)
            print('registro do piloto', [cont], ':', elemento.registroPiloto)
            print('nome',[cont],':',elemento.nomePiloto)
            print('data de nascimento', [cont], ':', elemento.nascimentoPiloto)
            print('horas de voo', [cont], ':', elemento.qtddVoo)
            print('email', [cont], ':', elemento.emailPiloto)
            print('telefone do piloto', [cont], ':', elemento.telefonePiloto)
            print('--' * 30)

def RelatorioViagem():
    data_inicio = input("Digite a primeira data: (d/m/yyyy)")
    print(data_inicio)

    di = datetime.strptime(data_inicio, "%d/%m/%Y")

    data_fim = input("Digite a segunda data: (d/m/yyyy)")
    print(data_fim)

    df = datetime.strptime(data_fim, "%d/%m/%Y")
    cont = 0
    for i in listaViagem:
        cont = cont + 1
        data_testar = i.data
        dt = datetime.strptime(data_testar, "%d/%m/%Y")
        if (dt < di):
            print("Viagem não encontrada")
        elif (dt == di):
            print("Viagem não encontrada")
        elif (dt > di and dt < df):
            print('--' * 30)
            print('Numero do voo', [cont], ':', i.numeroVoo)
            print('Piloto', [cont], ':', i.piloto)
            print('Data da partida', [cont], ':', i.data)
            print('Hora da partida', [cont], ':', i.hora)
            print('Quantidade de passageiros', [cont], ':', i.qtddPassageiros)
            for elemento in ListaPilotos:
                if elemento.nomePiloto == i.piloto:
                    print('registro piloto', [cont], ':', elemento.registroPiloto)
            for elemento in listaVoo:
                if elemento.numeroVoo1 == i.numeroVoo:
                    print('Cidade origem', [cont], ':', elemento.cidadeOrigem)
                    print('Cidade destino', [cont], ':', elemento.cidadeDestino)
                    print('Tempo medio', [cont], ':', elemento.tempoMedio)
                    print('Aeronave: ', [cont], ':', elemento.aeronave)
                    print('Cidades escala: ', [cont], ':', elemento.cidadesEscala)
                    print('--' * 30)
        elif (dt == df):
            print("Viagem não encontrada")
        elif (dt > df):
            print("Viagem não encontrada")

def RelatorioVoo():
    cidades = input('digite a cidade de escala para ver os voos que passaram nela: ')
    for elemento in listaVoo:
        if cidades in elemento.cidadesEscala:
            print('--' * 30)
            print('numero do voo: ', elemento.numeroVoo1)
            print('cidade de origem: ', elemento.cidadeOrigem)
            print('cidade de destino: ', elemento.cidadeDestino)
            print('tempo medio do voo:', elemento.tempoMedio)
            print('nome da aeronave: ', elemento.aeronave)
            print('--' * 30)

#-------------------------------------------------ALteral e Excluir-----------------------------------------------------

def AlterarDadosPilotos():
    registro = input('Digite o registro do piloto que ira alterar: ')
    cont = 0
    for elemento in ListaPilotos:
        cont = cont + 1
        if elemento.registroPiloto == registro:
            print('1- nome piloto', [cont], ':', elemento.nomePiloto)
            print('2- data de nascimento', [cont], ':', elemento.nascimentoPiloto)
            print('3- horas de voo', [cont], ':', elemento.qtddVoo)
            print('4- email', [cont], ':', elemento.emailPiloto)
            print('5- telefone', [cont], ':', elemento.telefonePiloto)
            opcao = int(input('Digite a opcao a ser alterada: '))
            if opcao == 1:
                name = input('digite o novo nome: ')
                elemento.nomePiloto = name
                print('Alterado com sucesso.')
            elif opcao == 2:
                data = input('digite a nova data: (dd/mm/aaaa)')
                elemento.nascimentoPiloto = data
                print('Alterado com sucesso.')
            elif opcao == 3:
                voo = input('digite a nova quantidade de horas de voo: ')
                elemento.qtddVoo = voo
                print('Alterado com sucesso.')
            elif opcao == 4:
                email = input('digite o novo email do piloto: ')
                elemento.emailPiloto = email
                print('Alterado com sucesso.')
            elif opcao == 5:
                tell = input('digite o novo telefone do piloto: ')
                elemento.telefonePiloto = tell
                print('Alterado com sucesso.')
            else:
                print('Opção inválida')


def ExcluirDadosPilotos():
    registro = input('Digite o registro do piloto que deseja excluir: ')
    for elemento in ListaPilotos:
        if elemento.registroPiloto == registro:
            ListaPilotos.remove(elemento)

def AlterarDadosVoo():
    nVoo = input('Digite o numero do voo que deseja alterar o cadastro: ')
    cont = 0
    for elemento in listaVoo:
        cont = cont + 1
        if elemento.numeroVoo1 == nVoo:
            print('1- Cidade Origem', [cont], ':', elemento.cidadeOrigem)
            print('2- Cidade Destino', [cont], ':', elemento.cidadeDestino)
            print('3- Tempo medio', [cont], ':', elemento.tempoMedio)
            print('4- Aeronaves', [cont], ':', elemento.aeronave)
            print('5- Cidades escala', [cont], ':', elemento.cidadesEscala)
            opcao = int(input('Digite a opcao a ser alterada: '))
            if opcao == 1:
                cidadeO = input('digite a nova cidade de saida: ')
                elemento.cidadeOrigem = cidadeO
                print('Alterado com sucesso.')
            elif opcao == 2:
                cidadeD = input('digite a nova cidade de destino: ')
                elemento.cidadeDestino = cidadeD
                print('Alterado com sucesso.')
            elif opcao == 3:
                hr = input('digite o novo tempo medio(em numero inteiro): ')
                elemento.tempoMedio = hr
                print('Alterado com sucesso.')
            elif opcao == 4:
                name = input('digite o novo nome da aeronave: ')
                elemento.aeronave = name
                print('Alterado com sucesso.')
            elif opcao == 5:
                escala = input('digite as novas cidades da escala (igual mostrado): ')
                elemento.cidadesEscala = escala
            else:
                print('Opção inválida')

def ExcluirDadosVoo():
    nVoo = input('Digite o numero do voo que deseja excluir: ')
    for elemento in listaVoo:
        if elemento.numeroVoo1 == nVoo:
            listaVoo.remove(elemento)
            print('Cadastro removido com sucesso!')

def AlterarDadosViagem():
    nVoo = input('Digite o numero do voo que deseja alterar a viagem: ')
    cont = 0
    opcao = 0
    for elemento in listaViagem:
        cont = cont + 1
        if elemento.numeroVoo == nVoo:
            print('1- Piloto', [cont], ':', elemento.piloto)
            print('2- Data da partida', [cont], ':', elemento.data)
            print('3- Hora da partida', [cont], ':', elemento.hora)
            print('4- Quantidade de passageiros', [cont], ':', elemento.qtddPassageiros)
            opcao = int(input('Digite a opcao a ser alterada: '))
            if opcao == 1:
                name = input('digite o novo nome: ')
                elemento.piloto = name
                print('Alterado com sucesso.')
            elif opcao == 2:
                data = input('digite a nova data de partida: (d/m/yyyy)')
                elemento.data = data
                print('Alterado com sucesso.')
            elif opcao == 3:
                hr = input('digite a nova hora de partida: ')
                elemento.hora = hr
                print('Alterado com sucesso.')
            elif opcao == 4:
                qtdd = input('digite a nova quantidade de passageiros: ')
                elemento.qtddPassageiros = qtdd
                print('Alterado com sucesso.')
            else:
                print('Opção inválida')

def ExcluirDadosViagem():
    nVoo = input('Digite o numero do voo que deseja excluir: ')
    for elemento in listaViagem:
        if elemento.numeroVoo == nVoo:
            listaViagem.remove(elemento)

#------------------------------------------MENUS------------------------------------------------------------------------

def subMenuArq():
    print('1-Armazenar no arquivo')
    print('2-Carregar o arquivo')
    print('3-sair')

def subMenuRelatorio():
    print('1-Relatorio Pilotos')
    print('2-Relatorio Voos')
    print('3-Relatorio Viagem')
    print('4-Sair')

def subMenuViagem():
    print('1-Incluir dados da viagem')
    print('2-Listar todas as viagens')
    print('3-Listar um elemento especifico')
    print('4-Alterar')
    print('5-Excluir')
    print('6-Sair')

def subMenuVoo():
    print('1-Adicionar dados do voo')
    print('2-Listar todos os voos')
    print('3-Listar um elemento especifico')
    print('4-Alterar ')
    print('5-Excluir ')
    print('6-Sair')

def subMenuPiloto():
    print('1-Incluir dados do piloto')
    print('2-Listar todos pilotos')
    print('3-Listar um elemento especifico')
    print('4-Alterar ')
    print('5-Excluir ')
    print('6-Sair')

def criarMenu():
    print('1- Submenu piloto')
    print('2- Submenu voo')
    print('3- Submenu viagem')
    print('4- Submenu relatorio')
    print('5- Sair')

#----------------------------------------------------------------------------------------------------------------------#

if arqExiste("pilotos.txt"):
    arquivo = open('pilotos.txt', 'r')
    for linha in arquivo:
        linha = linha[:len(linha)-1]
        dados = linha.split(';')
        p = Piloto()
        p.registroPiloto = dados[0]
        p.nomePiloto = dados[1]
        p.nascimentoPiloto = dados[2]
        p.qtddVoo = dados[3]
        p.emailPiloto = dados[4]
        p.telefonePiloto = dados[5]
        ListaPilotos.append(p)
    arquivo.close()

if arqExiste("voo.txt"):
    arquivo = open('voo.txt', 'r')
    for linha in arquivo:
        linha = linha[:len(linha) - 1]
        dados = linha.split(';')
        v = Voo()
        v.numeroVoo1 = dados[0]
        v.cidadeOrigem = dados[1]
        v.cidadeDestino = dados[2]
        v.tempoMedio = dados[3]
        v.aeronave = dados[4]
        v.cidadesEscala = dados[5]
        listaVoo.append(v)
    arquivo.close()

if arqExiste("viagem.txt"):
    arquivo = open('viagem.txt', 'r')
    for linha in arquivo:
        linha = linha[:len(linha) - 1]
        dados = linha.split(';')
        g = Viagem()
        g.numeroVoo = dados[0]
        g.piloto = dados[1]
        g.data = dados[2]
        g.hora = dados[3]
        g.qtddPassageiros = dados[4]
        listaViagem.append(g)
    arquivo.close()

#----------------------------------------------------------------------------------------------------------------------#
opcao = -1
while opcao != 5:
    criarMenu()
    opcao = int(input('Digite a opcão: '))
    if opcao == 1:
        opcao2 = -1
        while opcao2 != 0:
            subMenuPiloto()
            opcao2 = int(input('Digite a opcão: '))
            if opcao2 == 1:
                cadastrarPiloto()
            elif opcao2 == 2:
                listarTodosPilotos()
            elif opcao2 == 3:
                listarElementoEspecificoPiloto()
            elif opcao2 == 4:
                AlterarDadosPilotos()
            elif opcao2 == 5:
                ExcluirDadosPilotos()
            elif opcao2 == 6:
                break
            else:
                print('digite novamente, opcão não encontrado')
    elif opcao == 2:
        opcao3 = -1
        while opcao3 != 0:
            subMenuVoo()
            opcao3 = int(input('Digite a opcão: '))
            if opcao3 == 1:
                cadastrarVoo()
            elif opcao3 == 2:
                listarTodosVoos()
            elif opcao3 == 3:
                listarElementoEspecificoVoo()
            elif opcao3 == 4:
                AlterarDadosVoo()
            elif opcao3 == 5:
                ExcluirDadosVoo()
            elif opcao3 == 6:
                break
            else:
                print('digite novamente, opcão não encontrado')
    elif opcao == 3:
        opcao4 = -1
        while opcao4 != 0:
            subMenuViagem()
            opcao4 = int(input('Digite a opcão: '))
            if opcao4 == 1:
                cadastrarViagem()
            elif opcao4 == 2:
                listarTodasViagens()
            elif opcao4 == 3:
                listarElementoEspecificoViagem()
            elif opcao4 == 4:
                AlterarDadosViagem()
            elif opcao4 == 5:
                ExcluirDadosViagem()
            elif opcao4 == 6:
                break
            else:
                print('digite novamente, opcão não encontrado')
    elif opcao == 4:
        opcao5 = -1
        while opcao5 != 0:
            subMenuRelatorio()
            opcao5 = int(input('Digite a opcão:'))
            if opcao5 == 1:
                RelatorioPiloto()
            if opcao5 == 2:
                RelatorioVoo()
            if opcao5 == 3:
                RelatorioViagem()
            elif opcao5 == 4:
                break
    elif opcao == 5:
        arquivo = open('pilotos.txt', 'w')
        for elemento in ListaPilotos:
            linha = str(
                elemento.registroPiloto) + ';' + elemento.nomePiloto + ';' + elemento.nascimentoPiloto + ';' + str(
                elemento.qtddVoo) + ';' + elemento.emailPiloto + ';' + elemento.telefonePiloto + '\n'
            arquivo.write(linha)
        arquivo.close()
        arquivo = open('voo.txt', 'w')
        for elemento in listaVoo:
            linha = str(elemento.numeroVoo1) + ';' + elemento.cidadeOrigem + ';' + elemento.cidadeDestino + ';' + str(
                elemento.tempoMedio) + ';' + elemento.aeronave + ';' + str(elemento.cidadesEscala) + '\n'
            arquivo.write(linha)
        arquivo.close()
        arquivo = open('viagem.txt', 'w')
        for elemento in listaViagem:
            linha = str(
                elemento.numeroVoo) + ';' + elemento.piloto + ';' + elemento.data + ';' + elemento.hora + ';' + str(
                elemento.qtddPassageiros) + '\n'
            arquivo.write(linha)
        arquivo.close()
        break
    else:
        print('digite novamente, opcão não encontrado')
