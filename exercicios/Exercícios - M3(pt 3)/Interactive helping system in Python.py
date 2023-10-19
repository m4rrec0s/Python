from time import sleep
cores = (
    '\033[0m',    # sem cor - 0
    '\033[1;40m',   # preto - 1
    '\033[1;41m',   # vermelho - 2
    '\033[1;42m',   # verde - 3
    '\033[1;43m',   # amarelo - 4
    '\033[1;44m',   # azul - 5
    '\033[1;45m',   # magenta - 6
    '\033[1;46m',   # ciano - 7
    '\033[7;37m',   # branco - 8
)

def titulo(txt, cor=0):
    '''
    -> Textos com cores e linhas de acordo com seuu tamanho.
    :param txt: (string) texto que vai receber a edição
    :param cor: (opcional) escolha a cor de fundo do seu texto
    :return: cores no terminal
    '''
    print(cores[cor], end='')
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)

def IntHelp(funçao):
    '''
    -> Sistema interativo de ajuda
    :param funçao: Digite o nome da função ou biblioteca
    :return: Explicação de uso da função/biblioteca usando o comando Help
    '''
    titulo('Acessando o Interactive Help', 5)
    print(cores[8], end='')
    s = help(funçao)
    print(cores[0], end='')
    return s
    sleep(2)

while True:
    titulo('SISTEMA DE AJUDA PYHELP', 4)
    a = input('Digite uma função ou biblioteca >> ')
    if a.upper() == 'FIM':
        break
    else:
        IntHelp(a)

sleep(0.6)
titulo('Volte sempre!', 2)
