import time
import sys
import cx_Oracle
import datetime
import json


def timer(tempo):
    if tempo == 10:
        print(f'Em {tempo} segundos o programa será fechado!')
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')

    elif tempo == 3:
        print(f'Em {tempo} segundos você voltará para fazer login!')
        print('-' * 100)
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')

    else:
        print(f'Em {tempo} segundos voltaremos para o menu incial...')
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')


def cpf_entrada():
    def validador_cpf(cpf):
        corpo_cpf = cpf[:9]
        digito_cpf = cpf[-2:]

        calculo_1 = 0
        calculo_2 = 0

        multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        for i, j in zip(multiplicacao, corpo_cpf):
            calculo_1 += i * int(j)

        resto_1 = calculo_1 % 11

        digito_1 = 0 if resto_1 < 2 else 11 - resto_1

        corpo_cpf += str(digito_1)

        for i, j in zip(multiplicacao, corpo_cpf[1:]):
            calculo_2 += i * int(j)

        resto_2 = calculo_2 % 11

        digito_2 = 0 if resto_2 < 2 else 11 - resto_2

        return digito_cpf == f'{digito_1}{digito_2}'

    blocklist = [
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999'
    ]

    while True:
        cpf_inserido = input('Por favor digite seu CPF ou insira "X" para sair:')
        print('-' * 100)
        cpf_sem_barra = cpf_inserido.replace('-', '')
        cpf_formatado = cpf_sem_barra.replace('.', '')

        if cpf_formatado.isnumeric():
            if len(cpf_formatado) == 11:
                if cpf_formatado in blocklist:
                    print('O CPF não pode conter todos números iguais!\n')
                else:
                    if not validador_cpf(cpf_formatado):
                        print('Seu CPF está invalido\n')
                    else:
                        return cpf_formatado

            else:
                print('O CPF deve conter 11 dígitos!\n')

        elif cpf_formatado.lower() == 'x':
            return cpf_formatado

        else:
            print('Digite seu CPF corretamente ou apenas "x" para sair!\n')


def conexao_oracle():
    usuario = 'rm550269'
    senha = '291103'
    host = 'oracle.fiap.com.br'
    sid = 'ORCL'
    porta = '1521'

    try:
        credenciais = cx_Oracle.makedsn(host, porta, sid)
        conexao = cx_Oracle.connect(usuario, senha, credenciais)
        print("Conexão com o banco de dados Oracle estabelecida com sucesso.")
        return conexao
    except cx_Oracle.Error as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        return None


def conexao_close(conexao):
    try:
        if conexao:
            conexao.close()
            print("Conexão fechada.")
    except cx_Oracle.Error as e:
        print(f"Erro ao fechar a conexão: {e}")


def login():
    print('-' * 100)
    print('Bem vindo a RebocAI!')
    print('-' * 100)

    cpf_usuario = cpf_entrada()

    if cpf_usuario.lower() == 'x':
        return 1
    else:
        return cpf_usuario


def abertura_sinistro():
    def endereco_sinistro():
        while True:
            rua = input('Por favor digite a rua de onde o veiculo está: ')
            if rua.isnumeric():
                print('Por favor não utilize numeros na hora de digitar a rua! ')
            else:

                while True:
                    numero = input('Por favor digite o numero ou o km onde o veiculo esta: ')
                    if numero.isnumeric():
                        while True:
                            cep = input('Por favor digite seu cep: ')
                            cep_formatado = cep.replace('-', '')
                            if cep_formatado.isnumeric():
                                if len(cep_formatado) == 8:

                                    endereco = {
                                        'rua': rua,
                                        'numero': numero,
                                        'cep': cep
                                    }
                                    return endereco

                                else:
                                    print('O cep deve conter 8 digitos')

                            else:
                                print('Por favor utilize apenas numeros para digitar o cep!')
                    else:
                        print('Por favor utilize numeros na hora de informar o numero/km!')

    def tipo_sinistro():
        while True:
            escolha_usuario = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if escolha_usuario.isnumeric():
                if 5 > int(escolha_usuario) > 0:
                    return escolha_usuario

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)

    print('-' * 100)
    print('Vamos começar com seu endereço!')
    endereco_usuario = endereco_sinistro()

    print('-' * 100)
    print('O que aconteceu com seu veiculo?: ')
    print('[1] - Pane eletrica;\n'
          '[2] - Capotamento;\n'
          '[3] - Desastre natural;\n'
          '[4] - Batida;\n')

    escolha_sinistro = tipo_sinistro()

    if escolha_sinistro == '1':
        print('-' * 100)
        print('Otimo! de acordo acordo com o modelo do seu veiculo,'
              'estamos enviando um mecanico que chegará em menos de 20 minutos de moto com uma nova bateria!')

        data = datetime.datetime.now()

        registrar_sinistro = {
            'tipo': 'Pane eletrica',
            'data': (str(data)),
            'endereco': endereco_usuario,
            'img_moto_pane': 'dados_ia/img_guinchos/moto_pane_eletrica.jpg'
        }
        registros['registro_sinistro'] = registrar_sinistro

        with open('registros.json', 'w') as file:
            json.dump(registros, file, indent=4)

        timer(4)
        return True



    elif escolha_sinistro == '2':
        print('Otimo! Seu veiculo estava carregado?\n[1] Sim\n[2] Não')

        while True:
            carregado = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if carregado.isnumeric():
                if carregado == '1':

                    while True:
                        peso = input('Por favor digite o peso da carga em toneladas: ')
                        if peso.isnumeric():
                            print('Ok! Estamos enviando um modal de acordo com o peso da sua carga!')

                            data = datetime.datetime.now()

                            registrar_sinistro = {
                                'tipo': 'Capotamento',
                                'peso_carga': peso,
                                'data': (str(data)),
                                'endereco': endereco_usuario,
                                'img_guincho': 'dados_ia/img_guinchos/guincho_06.jpg'
                            }
                            registros['registro_sinistro'] = registrar_sinistro

                            with open('registros.json', 'w') as file:
                                json.dump(registros, file, indent=4)

                            timer(4)
                            return True

                        else:
                            print('Por favor utilize apenas numeros para digitar o peso!')


                elif carregado == '2':
                    print(
                        'Ok! Estamos mandando um Modal de acordo com o modelo do seu veiculo')
                    data = datetime.datetime.now()

                    registrar_sinistro = {
                        'tipo': 'Capotamento',
                        'data': (str(data)),
                        'endereco': endereco_usuario,
                        'img_guincho': 'dados_ia/img_guinchos/guincho_17.jpg'
                    }

                    registros['registro_sinistro'] = registrar_sinistro

                    with open('registros.json', 'w') as file:
                        json.dump(registros, file, indent=4)

                    timer(4)
                    return True

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)

    elif escolha_sinistro == '3':
        print('Otimo! Seu veiculo estava carregado?\n[1] Sim\n[2] Não')

        while True:
            carregado = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if carregado.isnumeric():
                if carregado == '1':

                    while True:
                        peso = input('Por favor digite o peso da carga em toneladas: ')
                        if peso.isnumeric():
                            print('Ok! Estamos enviando um modal de acordo com o peso da sua carga!')

                            data = datetime.datetime.now()

                            registrar_sinistro = {
                                'tipo': 'Desastre natural',
                                'peso_carga': peso,
                                'data': (str(data)),
                                'endereco': endereco_usuario,
                                'img_guincho': 'dados_ia/img_guinchos/guincho_06.jpg'
                            }
                            registros['registro_sinistro'] = registrar_sinistro

                            with open('registros.json', 'w') as file:
                                json.dump(registros, file, indent=4)

                            timer(4)
                            return True

                        else:
                            print('Por favor utilize apenas numeros para digitar o peso!')


                elif carregado == '2':
                    print(
                        'Ok! Estamos mandando um Modal de acordo com o modelo do seu veiculo')
                    data = datetime.datetime.now()

                    registrar_sinistro = {
                        'tipo': 'Desastre natural',
                        'data': (str(data)),
                        'endereco': endereco_usuario,
                        'img_guincho': 'dados_ia/img_guinchos/guincho_17.jpg'
                    }

                    registros['registro_sinistro'] = registrar_sinistro

                    with open('registros.json', 'w') as file:
                        json.dump(registros, file, indent=4)

                    timer(4)
                    return True

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)

    elif escolha_sinistro == '4':
        print('Otimo! Seu veiculo estava carregado?\n[1] Sim\n[2] Não')

        while True:
            carregado = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if carregado.isnumeric():
                if carregado == '1':

                    while True:
                        peso = input('Por favor digite o peso da carga em toneladas: ')
                        if peso.isnumeric():
                            print('Ok! Estamos enviando um modal de acordo com o peso da sua carga!')

                            data = datetime.datetime.now()

                            registrar_sinistro = {
                                'tipo': 'Batida',
                                'peso_carga': peso,
                                'data': (str(data)),
                                'endereco': endereco_usuario,
                                'img_guincho': 'dados_ia/img_guinchos/guincho_06.jpg'
                            }
                            registros['registro_sinistro'] = registrar_sinistro

                            with open('registros.json', 'w') as file:
                                json.dump(registros, file, indent=4)

                            timer(4)
                            return True

                        else:
                            print('Por favor utilize apenas numeros para digitar o peso!')


                elif carregado == '2':
                    print(
                        'Ok! Estamos mandando um Modal de acordo com o modelo do seu veiculo')
                    data = datetime.datetime.now()

                    registrar_sinistro = {
                        'tipo': 'Batida',
                        'data': (str(data)),
                        'endereco': endereco_usuario,
                        'img_guincho': 'dados_ia/img_guinchos/guincho_17.jpg'
                    }

                    registros['registro_sinistro'] = registrar_sinistro

                    with open('registros.json', 'w') as file:
                        json.dump(registros, file, indent=4)

                    timer(4)
                    return True

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)


def dados_cadastro(item):
    if item == 'nome':
        while True:
            nome = input('Digite o seu primeiro nome: ')
            if nome.isnumeric():
                print('Não utilize numeros na hora de cadastrar o nome!')
            else:
                return nome

    elif item == 'veiculo':
        while True:
            veiculo = input('Digite o modelo do seu veiculo: ')
            if veiculo.isnumeric():
                print('Não utilize numeros na hora de cadastrar o veiculo!')
            else:
                return veiculo

    elif item == 'largura':
        while True:
            largura = input('Digite a largura do seu veiculo arredondada em metros: ')
            if largura.isnumeric():
                return int(largura)
            else:
                print('por favor utilize numeros para digitar a largura')

    elif item == 'altura':
        while True:
            altura = input('Digite a altura do veiculo arredondada em metros: ')
            if altura.isnumeric():
                return int(altura)
            else:
                print('Por favor não utilize letras na hora cadastrar a altura')

    elif item == 'chassi':
        while True:
            chassi = input('Digite o modelo do seu chassi: ')
            if len(chassi) < 20:
                return chassi
            else:
                print('Seu chassi deve conter no maximo 20 caracteres!!!')

    elif item == 'numero':
        while True:
            numero = input('Digite o seu numero de telefone: ')
            if numero.isnumeric():
                return int(numero)
            else:
                print('Por favor não utilize letras na hora cadastrar o seu número')

    elif item == 'ano':
        while True:
            ano = input('Digite o ano do seu veiculo com 4 caracteres (Ex: 2023): ')
            if ano.isnumeric() and len(ano) == 4:
                return int(ano)
            else:
                print('Por favor urilize 4 caracteres, sendo todos eles numericos!')

    elif item == 'apolice':
        while True:
            print('[1] Multirisco;\n'
                  '[2] Risco nomeado;\n'
                  '[3] Apolice de recibo\n')
            apolice_num = input('Digite o numero da apolice que deseja cadastrar: ')
            if apolice_num.isnumeric():

                if 4 > int(apolice_num) > 0:
                    if int(apolice_num) == 1:
                        apolice = 'Multirisco'
                        return apolice
                    elif int(apolice_num) == 2:
                        apolice = 'Risco nomeado'
                        return apolice
                    elif int(apolice_num) == 3:
                        apolice = 'Apolice de recibo'
                        return apolice

                else:
                    print('Por favor escolha somente as opções acima')
            else:
                print('Utilize numeros na hora da escolha ')


def cadastro(id, conexao):
    def insert_veiculo(conexao, sql, id_bd, veiculo, chassi, ano, altura, largura):
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, valor1=id_bd, valor2=veiculo, valor3=chassi, valor4=ano, valor5=altura, valor6=largura)
            conexao.commit()
            print("Dados inseridos com sucesso.")
        except cx_Oracle.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def insert_usuario(conexao, sql, id_bd, nome, numero, apolice):
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, valor1=id_bd, valor2=nome, valor3=numero, valor4=apolice)
            conexao.commit()
            print("Dados inseridos com sucesso.")
        except cx_Oracle.Error as e:
            print(f"Erro ao inserir dados: {e}")

    print('-' * 100)
    print('Percebemos que seu CPF não possui cadastro no nosso sistema!\n'
          'Iremos te cadastrar neste exato momento! ')
    print('-' * 100)

    nome = dados_cadastro('nome')
    veiculo = dados_cadastro('veiculo')
    largura = dados_cadastro('largura')
    altura = dados_cadastro('altura')
    chassi = dados_cadastro('chassi')
    numero = dados_cadastro('numero')
    ano = dados_cadastro('ano')
    apolice = dados_cadastro('apolice')

    id_bd = id

    sql_veiculo = "INSERT INTO TB_PSG_TIPO_VEICULO (ID_TIPO_VEICULO, MODELO_VEICULO, TIPO_CHASSI_VEICULO, ANO_FABRICACAO_VEICULO, ALTURA_VEICULO, LARGURA_VEICULO) VALUES (:valor1, :valor2, :valor3,:valor4, :valor5, :valor6)"

    sql_usuario = "INSERT INTO TB_USUARIO (ID_USUARIO, NOME_USUARIO, TELEFONE_USUARIO, TIPO_APOLICE) VALUES (:valor1, :valor2, :valor3,:valor4)"

    insert_usuario(conexao, sql_usuario, id_bd, nome, numero, apolice)
    insert_veiculo(conexao, sql_veiculo, id_bd, veiculo, chassi, ano, altura, largura)

    print('-' * 100)
    print((' ' * 30) + 'Seus dados foram cadastrados com sucesso!')
    print('-' * 100)
    timer(3)


def mostrar_dados(conexao):
    def select(conexao, sql):
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except cx_Oracle.Error as e:
            print(f'Erro ao selecionar dados: {e}')

    select_usuario = f'SELECT * FROM TB_USUARIO'
    select_veiculo = f'SELECT * TB_PSG_TIPO_VEICULO'

    select(conexao, select_usuario)
    select(conexao, select_veiculo)

    print('-' * 100)


def escolha_dados():
    print('Escolha qual dado você deseja alterar: ')
    print('[0] - Largura do veiculo;\n'
          '[1] - Veiculo;\n'
          '[2] - Altura do veiculo;\n'
          '[3] - Chassi;\n'
          '[4] - Ano;\n')
    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)
        if escolha_usuario.isnumeric():
            if 5 > int(escolha_usuario) >= 0:
                if int(escolha_usuario) == 0:
                    return 'largura'
                elif int(escolha_usuario) == 1:
                    return 'veiculo'
                elif int(escolha_usuario) == 2:
                    return 'altura'
                elif int(escolha_usuario) == 3:
                    return 'chassi'
                elif int(escolha_usuario) == 4:
                    return 'ano'
            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)
        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)


def alterar_dados(id, conexao):
    def update(conexao, sql):
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            conexao.commit()
            print("Dados atualizados com sucesso.")
        except cx_Oracle.Error as e:
            print(f"Erro ao atualizar dados: {e}")

    escolha = {
        'largura': 'LARGURA_VEICULO',
        'veiculo': 'MODELO_VEICULO',
        'altura': 'ALTURA_VEICULO',
        'chassi': 'TIPO_CHASSI_VEICULO',
        'ano': 'ANO_FABRICACAO_VEICULO'
    }
    dado_para_mudar = escolha_dados()

    dado_alterado = dados_cadastro(dado_para_mudar)

    sql_veiculo = f'UPDATE TB_PSG_TIPO_VEICULO SET {escolha[dado_para_mudar]} = {dado_alterado} WHERE ID_TIPO_VEICULO = {id}'

    update(conexao, sql_veiculo)


def delete_dados(conexao):
    delete_veiculo = f'DELETE FROM TB_PSG_TIPO_VEICULO'
    delete_usuario = f'DELETE FROM TB_USUARIO'

    try:
        cursor = conexao.cursor()
        cursor.execute(delete_veiculo)
        cursor.execute(delete_usuario)
        conexao.commit()
        print("Dados deletados com sucesso.")
    except cx_Oracle.Error as e:
        print(f'Erro ao deletar dados: {e}')


def menu_inicial():
    print('-' * 100)
    print((' ' * 30) + 'MENU INICIAL')
    print('-' * 100)
    print('[0] Sair\n'
          '[1] Solicitar sinistro\n'
          '[2] Mostrar dados cadastrados\n'
          '[3] Alterar dados cadastrados\n'
          '[4] Deletar dados cadastrados\n')
    print('-' * 100)

    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)

        if escolha_usuario.isnumeric():
            if 5 > int(escolha_usuario) >= 0:
                return escolha_usuario

            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)


registros = {}

id_cpf = login()

if id_cpf == 1:
    print("Você escolheu sair!")
    timer(10)

else:
    conexao = conexao_oracle()
    cadastro(id_cpf, conexao)
    while True:
        menu = menu_inicial()
        if menu == '0':
            print('-' * 100)
            print('Voce escolheu sair')
            print('-' * 100)
            timer(10)
            conexao_close(conexao)
            break

        elif menu == '1':
            abertura_sinistro()


        elif menu == '2':
            mostrar_dados(conexao)
            timer(4)

        elif menu == '3':
            alterar_dados(id_cpf, conexao)
            timer(4)

        elif menu == '4':
            delete_dados(conexao)
            timer(4)

print('-' * 100)
print((' ' * 30) + 'Obrigado por usar a RebocAI! <3')
print('-' * 100)