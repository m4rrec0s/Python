#COVERSOR DE BASES NUMÉRICAS
num = int(input('Digite um número inteiro: '))

print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input(': '))

if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} cobertido para OCTAL é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inváçida!')