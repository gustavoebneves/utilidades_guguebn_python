def input_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except:
            print('\033[31mERRO! Valor inválido! Tente novamente!\033[m')
        else:
            return n

