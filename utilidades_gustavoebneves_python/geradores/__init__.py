def gerador_de_nomes(quant_sobrenom = 3):
    from random import choice

    nomes = ['Gustavo', 'Camila', 'Antônio', 'Aurora', 'Maria', 'Cecília', 'Laura', 'Liz', 'Rebeca', 'Ana', 'Mariana', 'Lúcia', 'Elisa', 'Miguel', 'Lucas', 'Pedro', 'Bruno', 'José', 'João', 'Davi', 'Guilherme', 'Arthur', 'Rafael', 'Daniel']

    lista_de_sobrenomes = ['Albuquerque', 'Almeida', 'Neves', 'Gorin', 'Barbosa', 'Bastos', 'Bernardes', 'Cardoso', 'Carmo', 'Carvalho', 'Castro', 'Coelho', 'Duarte', 'Silva', 'Andrade', 'Ferreira', 'Duarte', 'Dias', 'Freitas', 'Furtado', 'Gomes', 'Gonçalves', 'Lima', 'Lopes', 'Machado', 'Marques', 'Martins', 'Nunes', 'Nascimento', 'Oliveira', 'Pedrosa', 'Pereira', 'Pimentel', 'Ramos', 'Ribeiro', 'Rocha', 'Santana', 'Santos', 'Souza', 'Teixeira', 'Vieira']

    if quant_sobrenom > len(lista_de_sobrenomes) or quant_sobrenom < 0:
        print('\033[31mQuantidade de sobrenomes inválida!\033[m')

    else:
        primeiro_nome = choice(nomes)
        if quant_sobrenom == 0:
            sobrenome_completo = ''

        else:
            sobrenome = []

            for i in range(0, quant_sobrenom):
                sobrenome_temporário = choice(lista_de_sobrenomes)

                while sobrenome_temporário in sobrenome:
                    sobrenome_temporário = choice(lista_de_sobrenomes)
                sobrenome.append(sobrenome_temporário)

            sobrenome_completo = ' '.join(sobrenome)
    
        nome_completo = primeiro_nome + ' ' + sobrenome_completo
        return nome_completo
