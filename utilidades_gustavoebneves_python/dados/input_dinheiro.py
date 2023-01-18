def input_dinheiro(mensagem):
    valor = str(input(mensagem)).strip().replace(',', '.')
    while not valor.replace('.', '').isnumeric():  # apaga só aqui o ponto para checar se pode ser numérico
        print(f'\033[31mERRO! "{valor}" não é um valor inválido!\033[m\n')
        valor = str(input(mensagem)).strip().replace(',', '.')
    return float(valor)
