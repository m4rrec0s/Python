#pensando em um número
from random import randint

computador = randint(0, 10)
jogador = 999999
sair = 0
tentativas = 0

print('\033[32m==== O COMPUTADOR PENSOU EM UM NÚMERO ENTRE 0 E 10 ====\033[m')
while jogador != 0:
    jogador = int(input('Qual o número que o Computador pensou? '))
    tentativas += 1
    if jogador == computador:
        print(' ')
        print('\033[1;32mParabéns! Você acertou!\033[m (voce precisou de {} tentativas para acertar)'.format(tentativas))
        jogador = sair
    elif jogador > 10:
        print('\033[36mVocê digitou um número maior que 10, tente de novo!\033[m')
    elif jogador < 0:
        print('\033[35mVocê digitou um número menor que 1, tente de novo!\033[m')
    else:
        if jogador > computador:
            print('\033[31mMenos... tente novamente.\033[m')
        elif jogador < computador:
            print('\033[31mMais... tente novamente.\033[m')
