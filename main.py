print('Bem vindo a Porto!')


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


def sistema_entrada(x):

    while True:
        print('Olá! Seu atendimento de veiculos pesados será iniciado!')
        carroceria = input("Por favor digíte o tipo de carroceria do seu veículo:\n")
        if carroceria.isspace():
            print('Digite o tipo de carroceria do veiculo!\n')
        else:
            while True:
                altura_entrada = input('Para continuar, digite a altura do veiculo em metros:\n')
                altura_sem_ponto = altura_entrada.replace('.', '')
                altura = altura_sem_ponto.replace(',', '')

                if altura.isnumeric():
                    while True:
                        comprimento_entrada = input('Digite o comprimento do veiculo em metros:\n')
                        comprimento_sem_ponto = comprimento_entrada.replace('.', '')
                        comprimento = comprimento_sem_ponto.replace(',', '')

                        if comprimento.isnumeric():
                            while True:
                                chassi = input('Para continuar, digite o chassi do veiculo:\n')
                                if chassi.isspace():
                                    print('Por favor, digite o chassi!')
                                else:
                                    quantidade_de_eixos = input('Para continuar, digite a quantidade de eixos:\n')
                                    if quantidade_de_eixos.isnumeric():
                                        while True:
                                            print(f'Olá, verifique se suas informações estão corretas:\n'
                                                  f'CPF: {cpf_formatado}\n'
                                                  f'Comprimento: {comprimento_entrada}' + ' m\n'
                                                  f'Altura: {altura_entrada}' + ' m\n'
                                                  f'Chassi: {chassi}\n'
                                                  f'Eixos: {quantidade_de_eixos}\n'
                                                  f'Carroceria: {carroceria}\n'
                                                  f'Se estão corretas digite "1" , se não digite "2": ')
                                            digito_verificador = input()

                                            if digito_verificador.lower() == '1':
                                                while True:
                                                    print('Sua solicitação foi feita!')
                                                    nova_solicitacao = input('Para fazer uma nova '
                                                                             'solicitação digite "1",'
                                                                             ' se não digite "2":')
                                                    if nova_solicitacao.lower() == '2':
                                                        print('Obrigado por escolher a Porto!')
                                                        exit()
                                                    elif nova_solicitacao.lower() == '1':
                                                        print('Ok, Digite as informações para uma nova solicitação')
                                                        sistema_entrada(True)
                                                    else:
                                                        print('Não entendi! Digite o número novamente')

                                            elif digito_verificador.lower() == '2':
                                                print('Ok, digite novamente as informações novamente!')
                                                sistema_entrada(True)
                                            else:
                                                print('Não entendi! Digite o número novamente')

                                    elif quantidade_de_eixos.isspace():
                                        print('Por favor, digite a quantidade de eixos!')
                                    else:
                                        print('Por favor, utilize numeros para informar os eixos')

                        elif comprimento.isspace():
                            print('Por favor, digite o comprimento!')

                        else:
                            print('O comprimento deve ser digitado em numeros!')
                elif altura.isspace():
                    print("Por favor, utilize numeros!")
                else:
                    print('A altura deve ser utilizada numeros!')


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
    cpf_entrada = input('Para prosseguir com o atendimento, por favor digite seu CPF ou insira "X" para sair:')
    cpf_sem_barra = cpf_entrada.replace('-', '')
    cpf_formatado = cpf_sem_barra.replace('.', '')

    if cpf_formatado.isnumeric():
        if len(cpf_formatado) == 11:
            if cpf_formatado in blocklist:
                print('O CPF não pode conter todos números iguais!\n')
            else:
                if validador_cpf(cpf_formatado):
                    print('Seu CPF está valido!\n')
                    sistema_entrada(True)

                else:
                    print('Seu CPF está invalido\n')
        else:
            print('O CPF deve conter 11 dígitos!\n')
    elif cpf_formatado.lower() == 'x':
        break
    else:
        print('Digite seu CPF corretamente ou apenas "x" para sair!\n')

print('Atendimento encerrado!')
