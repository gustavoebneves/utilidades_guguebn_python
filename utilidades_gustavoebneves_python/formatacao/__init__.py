def print_center(mensagem, objeto = '-'):
    tamanho_msg = len(mensagem) + 4
    print(f'\033[1;30;42m{objeto * tamanho_msg:^156}' )
    print(f'\033[1;30;42m  {mensagem:^152}')            # para deixar centralizado no terminal do meu pc
    print(f'\033[1;30;42m{objeto * tamanho_msg:^156}' )
    print('\033[m', end='')


def especial_print(mensagem, objeto = '-'):
    tamanho_msg = len(mensagem) + 4
    print(f'{objeto * tamanho_msg}')
    print(f'  {mensagem}')
    print(f'{objeto * tamanho_msg}')
