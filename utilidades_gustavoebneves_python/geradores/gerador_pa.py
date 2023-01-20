def gerador_pa(prim_term = 1, razao = 1, gerar_lista = False):
    # Colocar mais opções
    # https://mundoeducacao.uol.com.br/matematica/progressao-aritmetica.htm
    nt = 0; opt = 1
    
    if gerar_lista: lista = list() 

    while opt != 0:
        if nt == 0:
            opt = int(input('\nVocê quer quantos termos da PA? '))
        else:
            opt = int(input('\nVocê quer quantos termos a mais? '))

        nt = 0
        while nt != opt:
            nt += 1
            print(prim_term, end=' -> ')

            if gerar_lista:
                lista.append(prim_term)

            prim_term += razao

        if opt != 0:
            print('Pausa')

    return lista


print(gerador_pa(1, 1, True))