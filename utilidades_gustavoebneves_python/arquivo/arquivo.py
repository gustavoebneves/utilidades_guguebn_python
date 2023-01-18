from utilidades_guguebn.formatacao import especial_print
def arquivo_existe(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')  # rt -> read + text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo_txt(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')  # wt+ -> write (editar) + text + plus (criar)
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo "{nome_arquivo}" criado com sucesso!')


def ler_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')  # rt -> read + text
    except:
        print('\033[31mHouve um erro na leitura do arquivo!\033[m')
    else:
        especial_print('LISTA DE PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()
