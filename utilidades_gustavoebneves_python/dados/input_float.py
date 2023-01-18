def input_real(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except:
            print('\033[31mERRO! Valor inválido! Tente novamente!\033[m')
        else:
            return n

