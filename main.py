print('-' * 20)
print('Bem vindo a Porto!')
print('-' * 100)

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

segurados = {
    '10184839939': {
            'Nome': 'Tanjiro Kamado',
            'Sexo': 'M',
            'Telefone': '11982415839',
            'Email': 'tanjiro.kamado@fiap.com.br',
            'Apólice': 'Multirrisco',
            'Veículo': 'VUC',
            'Eixos': '2',
            'Altura': '3,5 m',
            'Comprimento': '6,2 m',
            'Largura': '2,2 m',
            'Peso': '3,5 t'
        }
}
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

def abertura_de_sinistro():
    print('-' * 100)
    print('Olá, o acionamento do seguro será feito por aqui!')
    print('-' * 100)

    if cpf_formatado in segurados:

        while True:
            print(f'Olá {segurados[cpf_formatado]["Nome"]} Verificamos que sua apólice é de'
                  f' {segurados[cpf_formatado]["Apólice"]}\n')
            print('Por favor, nos diga o que aconteceu!')
            print('[0] Batida\n[1] Pane elétrica\n[2] Desatres naturais\n[3] Sair')
            escolha_usuario = input('Selecione uma das opções acima:')

            if escolha_usuario.isnumeric():
                    if escolha_usuario == '0':

                        print(f'A opção escolhida foi [{escolha_usuario}] Batida\n')
                        print('-' * 100)

                        print(f'Veículo: {segurados[cpf_formatado]["Veículo"]}\n'
                              f'Eixos: {segurados[cpf_formatado]["Eixos"]}\n'
                              f'Altura: {segurados[cpf_formatado]["Altura"]}\n'
                              f'Comprimento: {segurados[cpf_formatado]["Comprimento"]}\n'
                              f'Peso: {segurados[cpf_formatado]["Peso"]}\n'
                              f'Largura: {segurados[cpf_formatado]["Largura"]}\n')

                        digito_verificador = input('[1] Sim\n[2] Não\nSuas informações estão corretas?:')
                        if digito_verificador.isnumeric():
                            if digito_verificador == '1':
                                return True

                            elif digito_verificador == '2':
                                print('Por favor entre em contato com o nosso SAC para alterar sua apólice')
                                return False
                        else:
                            print('Por favor utilize números na hora da escolha!')

                    elif escolha_usuario == '1':
                        print(f'A opção escolhida foi [{escolha_usuario}] Pane elétrica\n')
                        print('-' * 100)

                        print(f'Veículo: {segurados[cpf_formatado]["Veículo"]}\n'
                              f'Eixos: {segurados[cpf_formatado]["Eixos"]}\n'
                              f'Altura: {segurados[cpf_formatado]["Altura"]}\n'
                              f'Comprimento: {segurados[cpf_formatado]["Comprimento"]}\n'
                              f'Peso: {segurados[cpf_formatado]["Peso"]}\n'
                              f'Largura: {segurados[cpf_formatado]["Largura"]}\n')

                        digito_verificador = input('[1] Sim\n[2] Não\nSuas informações estão corretas?:')
                        if digito_verificador.isnumeric():
                            if digito_verificador == '1':
                                solicitar_guincho = True
                                break

                            elif digito_verificador == '2':
                                solicitar_guincho = False
                                print('Por favor entre em contato com o nosso SAC para alterar sua apólice')
                                break

                        else:
                            print('Por favor utilize números na hora da escolha!')

                    elif escolha_usuario == '2':
                        print(f'A opção escolhida foi [{escolha_usuario}] Desastres naturais\n')
                        print('-' * 100)
                        print(f'Veículo: {segurados[cpf_formatado]["Veículo"]}\n'
                              f'Eixos: {segurados[cpf_formatado]["Eixos"]}\n'
                              f'Altura: {segurados[cpf_formatado]["Altura"]}\n'
                              f'Comprimento: {segurados[cpf_formatado]["Comprimento"]}\n'
                              f'Peso: {segurados[cpf_formatado]["Peso"]}\n'
                              f'Largura: {segurados[cpf_formatado]["Largura"]}\n')

                        digito_verificador = input('[1] Sim\n[2] Não\nSuas informações estão corretas?:')
                        if digito_verificador.isnumeric():
                            if digito_verificador == '1':
                                solicitar_guincho = True
                                break

                            elif digito_verificador == '2':
                                solicitar_guincho = False
                                print('Por favor entre em contato com o nosso SAC para alterar sua apólice')
                                break

                        else:
                            print('Por favor utilize números na hora da escolha!')

                    elif escolha_usuario == '3':
                        print(f'A opção escolhida foi [{escolha_usuario}] Sair\n')
                        break
                    else:
                        print('Por favor escolha apenas as opções listadas acima!')
            else:
                print('Por favor utilize números na hora da escolha!')

    else:
        print('Você não tem nenhuma apolice cadastrada!')


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
                    print('-' * 100)
                    print('Seu CPF está valido!')
                    print('-' * 100)
                    abertura_de_sinistro()
                    break
                else:
                    print('Seu CPF está invalido\n')
        else:
            print('O CPF deve conter 11 dígitos!\n')
    elif cpf_formatado.lower() == 'x':
        break
    else:
        print('Digite seu CPF corretamente ou apenas "x" para sair!\n')

print('Atendimento encerrado!')
