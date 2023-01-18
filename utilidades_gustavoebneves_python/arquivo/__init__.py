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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')

    finally:
        a.close()


def editar_arquivo(nome_arquivo, primeiro = '<unknown>', segundo = '<unknown>', terceiro = '<unknown>'):
    try:
        a = open(nome_arquivo, 'at')  # at -> append (adicionar coisas) + text
    except:
        print(f'\033[31mHouve um erro na abertura do arquivo "{nome_arquivo}"!\033[m')
    else:
        try:
            a.write(f'{primeiro};{segundo}\n')
        except:
            print('\033[31mHouve um erro ao editar o arquivo!\033[m')
        
    finally:
        a.close()
