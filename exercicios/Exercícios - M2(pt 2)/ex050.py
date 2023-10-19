# PAR OU IMPAR
# 1 - perguntar o numero e se é impar ou par, 2 - calcular numero, 3 - verificar se foi impar ou par, 4 - ganhou ou perdeu

from random import randint
cont = 0
jogo = ' ¿ IMPAR OU PAR ? '
print('\033[34m--\033[m'*25)
print(f'\033[1;33m{ jogo :-^50}')
print('\033[31m--\033[m'*25)
while True:
    computador = randint(1, 10)
    numero = int(input('Digite um número: '))
    pi = str(input('IMPAR OU PAR? [I/P]: ')).upper().strip()[0]
    print('--' * 25)
    soma = computador + numero
    print(f'\033[1;33mComputador\033[m jogou {computador}')
    print(f'\033[1;34mJogador\033[m jogou {numero}')
    if soma %2 == 0:
        print(f'{soma} é \033[34mPAR\033[m')
        print('--' * 25)
        if pi == 'P':
            cont += 1
            print('\033[1;32mJOGADOR GANHOU\033[m')
            print('Vamos novamente....')
            print('--' * 25)
        elif pi == 'I':
            print('\033[1;31mJOGADOR PERDEU\033[m')
            print(f'Você ganhou \033[1;34m{cont}\033[m vezes!!')
            break
    else:
        print(f'{soma} é \033[1;37mIMPAR\033[m')
        print('--' * 25)
        if pi == 'P':
            print('\033[1;31mJOGADOR PERDEU!\033[m')
            print('--' * 25)
            print(f'Você ganhou \033[1;34m{cont}\033[m vezes!!')
            break
        elif pi == 'I':
            cont += 1
            print('\033[1;32mJOGADOR GANHOU!\033[m')
            print('Vamos novamente....')
            print('--' * 25)
fim = ' FIM '
print('\033[31m--\033[m'*25)
print(f'\033[1;33m{fim:-^50}\033[m')
print('\033[34m--\033[m'*25)
