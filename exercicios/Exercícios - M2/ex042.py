#calculadora

voltar = 10
sair = False

opcao = 0

while not sair:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('='*20)

    opcao = 0

    while opcao != voltar:
        opcao = int(input('''O que deseja fazer?
[1] somar
[2] multiplicar
[3] maior valor
[4] novos números
[5] sair do programa
        
-> '''))
        print('='*20)
        soma = n1 + n2
        multiplicação = n1 * n2

        if opcao == 1:
            print('{} + {} = {}'.format(n1, n2, soma))
        elif opcao == 2:
            print('{} x {} = {}'.format(n1, n2, multiplicação))
        elif opcao == 3:
            print('O maior valor entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
        elif opcao == 4:
            print('Ok! digite novos números!')
            opcao = voltar
        elif opcao == 5:
            print('Até mais!')
            sair = True
            break
        else:
            print('caractére inválido, tente novamente.')
        print('='*20)
