def aumentar(dinheiro, form=False, quant=0):
    """
    -> Calcula o aumento de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna o aumento 'aumento'.
    """
    if quant == 0:
        quant = int(input(f'Em quantos % você quer aumentar seus {dinheiro} reais? '))
    aumento = dinheiro + (dinheiro * (quant/100))
    return aumento if not form else moeda(aumento)


def diminuir(dinheiro, form=False, quant=0):
    """
    -> Calcula a diminuição de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna a diminuição 'diminuição'.
    """
    if quant == 0:
       quant = int(input(f'Em quantos % você quer diminuir seus {dinheiro} reais? '))
    diminuicao = dinheiro - (dinheiro * (quant/100))
    return diminuicao if not form else moeda(diminuicao)


def dobrar(dinheiro, form=False):
    """
    -> Calcula o dobro de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna o dobro de 'dinheiro'.
    """
    dobro = dinheiro * 2
    return dobro if not form else moeda(dobro)


def metade(dinheiro, form=False):
    """
    -> Calcula a metade de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna a metade de 'dinheiro'.
    """
    metadinha = dinheiro / 2
    return metadinha if not form else moeda(metadinha)

def moeda(dinheiro):
    """
    -> Formata um valor em reais com duas casas decimais após o ponto.
    :param dinheiro: Valor inserido.
    :return: Valor formatado.
    """
    # fazer o input da moeda real euro dolar
    valor = f'R$ {dinheiro:.2f}'.replace('.', ',')
    return valor


def resumo(dinheiro=0, aumento=0, diminuicao=0):
    print('='*54)
    print(f'{"RESUMO DO VALOR":^54}')
    print('='*54)
    print(f'''Valor analisado: \t{moeda(dinheiro)}
Dobro do valor: \t{dobrar(dinheiro, True)}
Metade do valor: \t{metade(dinheiro, True)}
Com aumento: \t\t{aumentar(dinheiro, True, aumento)}
Com diminuição: \t{diminuir(dinheiro, True, diminuicao)}''')
    print('='*54)
