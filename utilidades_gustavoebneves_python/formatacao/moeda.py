def aumentar(dinheiro, quant=0, form=False, pais = 'R$'):
    """
    -> Calcula o aumento de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna o aumento 'aumento'.
    """
    if quant == 0:
        quant = int(input(f'Em quantos % você quer aumentar seus {dinheiro} reais? '))
    aumento = dinheiro + (dinheiro * (quant/100))
    return aumento if not form else moeda(aumento, pais)


def diminuir(dinheiro, quant=0, form=False, pais = 'R$'):
    """
    -> Calcula a diminuição de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna a diminuição 'diminuição'.
    """
    if quant == 0:
       quant = int(input(f'Em quantos % você quer diminuir seus {dinheiro} reais? '))
    diminuicao = dinheiro - (dinheiro * (quant/100))
    return diminuicao if not form else moeda(diminuicao, pais)


def dobrar(dinheiro, form=False, pais = 'R$'):
    """
    -> Calcula o dobro de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna o dobro de 'dinheiro'.
    """
    dobro = dinheiro * 2
    return dobro if not form else moeda(dobro, pais)


def metade(dinheiro, form=False, pais = 'R$'):
    """
    -> Calcula a metade de uma quantidade em dinheiro.
    :param dinheiro: Quantidade inserida pelo usuário.
    :return: Retorna a metade de 'dinheiro'.
    """
    metadinha = dinheiro / 2
    return metadinha if not form else moeda(metadinha, pais)

def moeda(dinheiro, pais = 'R$'):
    """
    -> Formata um valor em reais com duas casas decimais após o ponto.
    :param dinheiro: Valor inserido.
    :return: Valor formatado EM STRING.
    """

    valor = f'{pais} {dinheiro:.2f}'.replace('.', ',')
    return valor


def resumo(dinheiro=0, aumento=0, diminuicao=0, pais = 'R$'):
    print('='*54)
    print(f'{"RESUMO DO VALOR":^54}')
    print('='*54)
    print(f'''Valor analisado: \t{moeda(dinheiro, pais)}
Dobro do valor: \t{dobrar(dinheiro, True, 'US$')}
Metade do valor: \t{metade(dinheiro, True, 'US$')}
Com aumento: \t\t{aumentar(dinheiro, True, aumento, 'US$')}
Com diminuição: \t{diminuir(dinheiro, True, diminuicao, 'US$')}''')
    print('='*54)
