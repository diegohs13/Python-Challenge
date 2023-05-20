import time

print('-' * 100)
print('Bem vindo a Porto!')
print('-' * 100)


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

    if cpf_formatado in segurados:

        while True:
            print('-' * 100)
            print('Olá, o acionamento do seguro será feito por aqui!')
            print('-' * 100)

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
                          f'Placa: {segurados[cpf_formatado]["Placa"]}\n'
                          f'Eixos: {segurados[cpf_formatado]["Eixos"]}\n'
                          f'Altura: {segurados[cpf_formatado]["Altura"]}\n'
                          f'Comprimento: {segurados[cpf_formatado]["Comprimento"]}\n'
                          f'Peso: {segurados[cpf_formatado]["Peso"]}\n'
                          f'Largura: {segurados[cpf_formatado]["Largura"]}\n')

                    while True:
                        digito_verificador = input('[1] Sim\n[2] Não\nSuas informações estão corretas?:')
                        if digito_verificador.isnumeric():
                            if digito_verificador == '1':
                                return '0'

                            elif digito_verificador == '2':
                                print('-' * 100)
                                print('Por favor entre em contato com o nosso SAC para alterar sua apólice\n'
                                      'SAC: 11946236792')
                                print('-' * 100)
                                return ''

                            else:
                                print('-' * 100)
                                print('Por favor escolha somente as opções informadas!')

                        else:
                            print('¨' * 100)
                            print('Por favor utilize números na hora da escolha!')

                if escolha_usuario == '1':
                    print(f'A opção escolhida foi [{escolha_usuario}] Batida\n')
                    print('-' * 100)

                    print(f'Veículo: {segurados[cpf_formatado]["Veículo"]}\n'
                          f'Placa: {segurados[cpf_formatado]["Placa"]}\n'
                          f'Eixos: {segurados[cpf_formatado]["Eixos"]}\n'
                          f'Altura: {segurados[cpf_formatado]["Altura"]}\n'
                          f'Comprimento: {segurados[cpf_formatado]["Comprimento"]}\n'
                          f'Peso: {segurados[cpf_formatado]["Peso"]}\n'
                          f'Largura: {segurados[cpf_formatado]["Largura"]}\n')

                    while True:
                        digito_verificador = input('[1] Sim\n[2] Não\nSuas informações estão corretas?:')
                        if digito_verificador.isnumeric():
                            if digito_verificador == '1':
                                return '1'

                            elif digito_verificador == '2':
                                print('-' * 100)
                                print('Por favor entre em contato com o nosso SAC para alterar sua apólice\n'
                                      'SAC: 11946236792')
                                print('-' * 100)
                                return ''

                            else:
                                print('-' * 100)
                                print('Por favor escolha somente as opções informadas!')

                        else:
                            print('¨' * 100)
                            print('Por favor utilize números na hora da escolha!')

                if escolha_usuario == '2':
                    print(f'A opção escolhida foi [{escolha_usuario}] Batida\n')
                    print('-' * 100)

                    print(f'Veículo: {segurados[cpf_formatado]["Veículo"]}\n'
                          f'Placa: {segurados[cpf_formatado]["Placa"]}\n'
                          f'Eixos: {segurados[cpf_formatado]["Eixos"]}\n'
                          f'Altura: {segurados[cpf_formatado]["Altura"]}\n'
                          f'Comprimento: {segurados[cpf_formatado]["Comprimento"]}\n'
                          f'Peso: {segurados[cpf_formatado]["Peso"]}\n'
                          f'Largura: {segurados[cpf_formatado]["Largura"]}\n')

                    while escolha_usuario:
                        digito_verificador = input('[1] Sim\n[2] Não\nSuas informações estão corretas?:')
                        if digito_verificador.isnumeric():
                            if digito_verificador == '1':
                                return '2'

                            elif digito_verificador == '2':
                                print('-' * 100)
                                print('Por favor entre em contato com o nosso SAC para alterar sua apólice\n'
                                      'SAC: 11946236792')
                                print('-' * 100)
                                return ''

                            else:
                                print('-' * 100)
                                print('Por favor escolha somente as opções informadas!')

                        else:
                            print('¨' * 100)
                            print('Por favor utilize números na hora da escolha!')

                elif escolha_usuario == '3':
                    print('-' * 100)
                    print('Você escolheu sair!')
                    print('-' * 100)
                    return ''

                else:
                    print('-' * 100)
                    print('Por favor escolha apenas as opções listadas acima!')
                    print('-' * 100)

            else:
                print('-' * 100)
                print('Por favor utilize números na hora da escolha!')
                print('-' * 100)

    else:
        print('-' * 100)
        print('Você não tem nenhuma apolice cadastrada!\n'
              'Para cadastrar uma apolice, por favor entre no nosso site: https://www.portoseguro.com.br/')
        print('-' * 100)
        return ''


def solicitar_guincho(sinistro):
    print('-' * 100)
    print('Pediremos apenas mais algumas informações para concluir com a solicitação do guincho.')
    print('-' * 100 + '\n')

    if sinistro == 0:
        while True:
            veiculo_tombado = input('[1] sim\n[2] Não\nPoderia nos dizer se seu veiculo se encontra tombado?:')
            print('-' * 100)

            if veiculo_tombado.isnumeric():
                while True:
                    if veiculo_tombado == '1':
                        peso_carga_entrada = input('Digite o peso da carga que está sendo transportada em toneladas: ')
                        print('-' * 100)

                        if peso_carga_entrada.isnumeric():
                            peso_carga = float(peso_carga_entrada)

                            print(f'Ok! Estamos enviando um guincho para veículos tombados com cargas de '
                                  f'{peso_carga} toneladas')
                            print('-' * 100)
                            return ''

                        else:
                            print('Por favor utilize numeros para digitar o peso da carga')

                    elif veiculo_tombado == '2':
                        peso_carga_entrada = input('Digite o peso da carga que está sendo transportada em toneladas: ')
                        print('-' * 100)

                        if peso_carga_entrada.isnumeric():
                            peso_carga = float(peso_carga_entrada)

                            print(f'Ok! Estamos enviando um guincho para veículos cargas de '
                                  f'{peso_carga} toneladas')
                            print('-' * 100)
                            return ''

                        else:
                            print('Por favor utilize numeros para digitar o peso da carga')

                    else:
                        print('-' * 100)
                        print('Por favor escolha somente as opções dadas!')
                        print('-' * 100)
                        break
            else:
                print('Por favor digite numeros na hora da escolha\n')

    elif sinistro == 1:
        while True:
            bateria = input('[1] Bateria Comum\n'
                            '[2] Bataria de caminhões'
                            '\nPoderia nos dizer o tipo de bateria do seu veiculo?:')

            if bateria.isnumeric():
                while True:
                    if bateria == '1':
                        print('-' * 100)
                        print('Ok! Estamos enviando um motoboy com uma bateria comum para a troca!')
                        print('-' * 100)
                        return ''

                    elif bateria == '2':
                        print('-' * 100)
                        print('Ok! Estamos enviando um motoboy com uma bateria de caminhões para a troca! ')
                        print('-' * 100)
                        return ''
                    else:
                        print('-' * 100)
                        print('Por favor escolha somente as opções dadas!')
                        print('-' * 100)
                        break
            else:
                print('-' * 100)
                print('Por favor utilize numeros na hora da escolha')
                print('-' * 100)

    elif sinistro == 2:
        while True:
            desastres_naturais = input('[1] Árvore caída\n[2] Desmoronamento\n[3] Alagamento\n[4] Raio\n'
                                       'Por favor escolha uma das opções de acordo com o ocorrido:')

            if desastres_naturais.isnumeric():
                while True:
                    if desastres_naturais == '1':
                        print('-' * 100)
                        print('Ok! Estamos enviando um guincho para retirada de veículos atingido por árvores!')
                        print('-' * 100)
                        return ''

                    elif desastres_naturais == '2':
                        print('-' * 100)
                        print('Ok! Estamos enviando um guincho para veículos atingidos por desmoronamento!')
                        print('-' * 100)
                        return ''

                    elif desastres_naturais == '3':
                        print('-' * 100)
                        print('Ok! Estamos enviando um guincho para veículos alagados!')
                        print('-' * 100)
                        return ''

                    elif desastres_naturais == '4':
                        print('-' * 100)
                        print('Ok! Estamos enviando um guincho para seu veículo atingido!')
                        print('-' * 100)
                        return ''

                    else:
                        print('-' * 100)
                        print('Por favor escolha somente as opções dadas!')
                        print('-' * 100)
                        break
            else:
                print('-' * 100)
                print('Por favor utilize numeros na hora da escolha')
                print('-' * 100)
    else:
        print('Não entendemos sua solicitação, por favor entre em contato com nosso SAC\n'
              'SAC: 11946236792')


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
    '52733860801': {
            'Nome': 'Tanjiro Kamado',
            'Sexo': 'M',
            'Telefone': '11982415839',
            'Email': 'tanjiro.kamado@fiap.com.br',
            'Apólice': 'Multirrisco',
            'Placa': 'VCP2R90',
            'Veículo': 'VUC',
            'Eixos': '2',
            'Altura': '3,5 m',
            'Comprimento': '6,2 m',
            'Largura': '2,2 m',
            'Peso': '3,5 t'
        }
}

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
                    print('x' * 100)

                    tipo_sinistro_entrada = abertura_de_sinistro()

                    if tipo_sinistro_entrada.isnumeric():
                        tipo_sinistro = int(tipo_sinistro_entrada)

                        tipo_guincho = solicitar_guincho(tipo_sinistro)
                        print(tipo_guincho)
                        print('Em 10 segundos o atendimento será encerrado!')
                        time.sleep(10)
                        break

                    else:
                        print('Em 10 segundos o atendimento será encerrado')
                        time.sleep(10)
                        break

                else:
                    print('Seu CPF está invalido\n')

        else:
            print('O CPF deve conter 11 dígitos!\n')

    elif cpf_formatado.lower() == 'x':
        print('Em 10 segundos o atendimento será encerrado')
        time.sleep(10)
        break
    else:
        print('Digite seu CPF corretamente ou apenas "x" para sair!\n')

print('x' * 100)
print('Atendimento encerrado!')
print('x' * 100)
