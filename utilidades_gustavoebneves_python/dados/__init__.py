def input_dinheiro(mensagem):
    valor = str(input(mensagem)).strip().replace(',', '.')
    while not valor.replace('.', '').isnumeric():  # apaga só aqui o ponto para checar se pode ser numérico
        print(f'\033[31mERRO! "{valor}" não é um valor inválido!\033[m\n')
        valor = str(input(mensagem)).strip().replace(',', '.')
    return float(valor)


def input_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (TypeError, ValueError):
            print('\033[31mERRO! Valor inválido! Tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu encerrar o programa!\033[m\n')
            break
        else:
            return n


def input_float(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except:
            print('\033[31mERRO! Valor inválido! Tente novamente!\033[m')
        else:
            return n

