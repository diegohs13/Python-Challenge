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
                    while True:
                        print('Olá! Seu atendimento será iniciado!')

                        carroceria = input("Por favor digíte o tipo de carroceria do seu veículo:\n")

                        if carroceria:

                            altura = input(
                                'Para continuar, digite a altura do veiculo em centimetros ou "X" para sair:\n')

                            if altura.isnumeric():
                                print(altura)

                            elif altura.lower() == 'x':
                                break

                            else:
                                print('Digite a altura do veiculo ou "X" para sair!\n')

                        elif carroceria.lower() == 'x':
                            break
                        else:
                            print('Digite o tipo de carroceria do veiculo ou "X" para sair!\n')
                else:
                    print('Seu CPF está invalido\n')

        else:
            print('O CPF deve conter 11 dígitos!\n')

    elif cpf_formatado.lower() == 'x':
        break

    else:
        print('Digite seu CPF corretamente ou apenas "x" para sair!\n')


print('Atendimento encerrado!')
