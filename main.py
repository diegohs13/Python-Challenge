def timer(tempo):
    import time
    import sys

    if tempo == 10:
        print(f'Em {tempo} segundos o programa será fechado!')
        print('-' * 100)
        print((' ' * 30) + 'Obrigado por usar a RebocAI! <3')
        print('-' * 100)
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
            break
        else:
            print('Digite seu CPF corretamente ou apenas "x" para sair!\n')


def login():
    print('-' * 100)
    print('Bem vindo a RebocAI!')
    print('-' * 100)

    cpf_usuario = cpf_entrada()

    return True if cpf_usuario in segurados else cadastro(cpf_usuario)


def dados_cadastro(item):
    if item == 'nome':
        while True:
            nome = input('Digite o seu primeiro nome: ')
            if nome.isnumeric():
                print('Não utilize numeros na hora de cadastrar o nome!')
            else:
                return nome

    elif item == 'sobrenome':
        while True:
            sobrenome = input('Digite o seu sobrenome: ')
            if sobrenome.isnumeric():
                print('Não utilize numeros na hora de cadastrar o sobrenome!')
            else:
                return sobrenome

    elif item == 'veiculo':
        while True:
            veiculo = input('Digite o modelo do seu veiculo pesado: ')
            if veiculo.isnumeric():
                print('Não utilize numeros na hora de cadastrar o veiculo')
            else:
                return veiculo

    elif item == 'placa':
        while True:
            placa = input('Digite o seu numero da placa: ')
            if len(placa) == 7:
                return placa
            else:
                print('Sua placa deve conter 7 digitos')

    elif item == 'numero':
        while True:
            numero = input('Digite o seu numero de telefone: ')
            if numero.isnumeric():
                return numero
            else:
                print('Por favor não utilize letras na hora cadastrar o seu número')

    elif item == 'eixos':
        while True:
            eixo = input('Digite o seu numero de eixos: ')
            if eixo.isnumeric():
                return eixo
            else:
                print('Por favor não utilize letras na hora cadastrar o seu eixo')

    elif item == 'apolice':
        while True:
            print('[1] Multirisco;\n'
                  '[2] Risco nomeado;\n'
                  '[3] Apolice de recibo\n')
            apolice = input('Digite o numero da apolice que deseja cadastrar: ')
            if apolice.isnumeric():
                if int(apolice) > 3:
                    print('Por favor escolha somente as opções acima')
                elif int(apolice) <= 0:
                    print('Por favor escolha somente as opções acima')
                else:
                    return apolice
            else:
                print('Utilize numeros na hora da escolha ')


def cadastro(identificacao):
    print('-' * 100)
    print('Percebemos que seu CPF não possui cadastro no nosso sistema!\n'
          'Iremos te cadastrar neste exato momento! ')
    print('-' * 100)

    segurados_cadastro = {
        'nome': dados_cadastro('nome'),
        'sobrenome': dados_cadastro('sobrenome'),
        'veiculo': dados_cadastro('veiculo'),
        'placa': dados_cadastro('placa'),
        'numero': dados_cadastro('numero'),
        'eixos': dados_cadastro('eixos'),
        'apolice': dados_cadastro('apolice'),
    }

    segurados[identificacao] = segurados_cadastro
    print('-' * 100)
    print((' ' * 30) + 'Seus dados foram cadastrados com sucesso!')
    print('-' * 100)
    timer(3)


def mostrar_dados(id):
    if id in segurados:
        print(f'Seus dados cadastrados são:\n {segurados[id]}')
        print('-' * 100)
    else:
        print('Não existe nenhum dado cadastrado neste CPF')
        print('-' * 100)


def alterar_dados(id):

  def escolha_dados():
    print('Escolha qual dado você deseja alterar: ')
    print('[0] - Nome;\n'
      '[1] - Sobrenome;\n'
      '[2] - Veiculo;\n'
      '[3] - Placa;\n'
      '[4] - Numero telefone;\n'
      '[5] - Eixos;\n'
      '[6] - Apolice;\n')
    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)

        if escolha_usuario.isnumeric():
            if 7 > int(escolha_usuario) >= 0:
              lista = ['nome', 'sobrenome', 'veiculo', 'placa', 'numero', 'eixos','apolice']
              return lista[int(escolha_usuario)]

            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)

  if id in segurados:
    print(f'Seus dados cadastrados são:\n {segurados[id]}')
    print('-' * 100)

    dado_para_mudar = escolha_dados()

    dado_alterado = dados_cadastro(dado_para_mudar)

    segurados[id][dado_para_mudar] = dado_alterado


def menu_inicial():
    print('-' * 100)
    print((' ' * 30) + 'MENU INICIAL')
    print('-' * 100)
    print('[0] Sair\n'
          '[1] Solicitar sinistro\n'
          '[2] Mostrar dados cadastrados\n'
          '[3] Alterar dados cadastrados\n')
    print('-' * 100)

    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)

        if escolha_usuario.isnumeric():
            if 4 > int(escolha_usuario) >= 0:
                return escolha_usuario

            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)


segurados = {}

try:
    login()

except:
    print("Ocorreu um erro inesperado, por favor tente novamente!")

else:
    while True:
        menu = menu_inicial()

        if menu == '0':
            print('-' * 100)
            print('Voce escolheu sair')
            print('-' * 100)
            timer(10)
            break

        elif menu == '1':
            print(segurados)

        elif menu == '2':
            id_cpf = cpf_entrada()
            mostrar_dados(id_cpf)

        elif menu == '3':
            id_cpf = cpf_entrada()
            alterar_dados(id_cpf)


finally:
    print('obrigado por usar a RebocAI')
