def leiaInt(n):
    while True:
        try:
            v = int(input(n))
            return v
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar um valor inteiro!\033[m')
            return 0

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro várido!\033[m')


cores = ('\033[m',  # sem cor
         '\033[31m',  # vermelho
         '\033[1;33m',  # laranja
         '\033[33m',  # amarelo
         '\033[32m',  # verde
         '\033[34m',  # azul
         '\033[35m',  # roxo
         '\033[30m',  # preto
         '\033[37m')  # branco


def cabecalho(txt):
    print('—' * 50)
    print(f'{txt:^50}')
    print('—' * 50)

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores[2]}{c} -{cores[5]} {item}{cores[0]}')
        c += 1
    print('—' * 50)
    opc = leiaInt(f'{cores[2]}Sua opção: {cores[0]}')
    return opc

