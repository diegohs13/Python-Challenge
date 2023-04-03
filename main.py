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
                    print('Olá! Seu atendimento será iniciado!')

                    while True:
                        carroceria = input("Por favor digíte o tipo de carroceria do seu veículo:\n")
                        if carroceria.isspace():
                            print('Digite o tipo de carroceria do veiculo!\n')
                        else:
                            while True:
                                altura = input('Para continuar, digite'
                                               ' a altura do veiculo em centimetros:\n')

                                if altura.isnumeric():
                                    while True:
                                        comprimento = input('Digite o comprimento do veiculo em centimetros:\n')

                                        if comprimento.isnumeric():
                                            while True:
                                                chassi = input('Para continuar, digite o chassi do veiculo:\n')

                                                if chassi.isspace():
                                                    print('Por favor, digite o chassi!')

                                                else:
                                                    while True:

                                                        print(f'Olá, verifique se suas informações estão corretas:\n'
                                                              f'CPF: {cpf_formatado}\n'
                                                              f'Comprimento: {comprimento}\n'
                                                              f'Altura: {altura}\n'
                                                              f'Chassi: {chassi}\n'
                                                              f'Carroceria: {carroceria}\n'
                                                              f'Se estão corretas digite "sim" , se não '
                                                              f'digite qualquer outra coisa: ')
                                                        digito_verificador = input()

                                                        if digito_verificador.lower() == 'sim':
                                                            print('Sua solicitação foi feita!')
                                                            exit()
                                                        else:
                                                            print('Ok, digite as informações novamente!')
                                                            exit()

                                        elif comprimento.isspace():
                                            print('Por favor, digite o comprimento!')

                                        else:
                                            print('O comprimento deve ser digitado em numeros!')
                                elif altura.isspace():
                                    print("Por favor, utilize numeros!")
                                else:
                                    print('A altura deve ser utilizada apenas numeros!')
                else:
                    print('Seu CPF está invalido\n')
        else:
            print('O CPF deve conter 11 dígitos!\n')
    elif cpf_formatado.lower() == 'x':
        break
    else:
        print('Digite seu CPF corretamente ou apenas "x" para sair!\n')


print('Atendimento encerrado!')
