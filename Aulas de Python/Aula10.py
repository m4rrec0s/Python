num = [2, 6, 8, 1, 3]
num[2] = 7
num.append(12)
num.sort(reverse=True)
num.insert(0, 2)
if 2 in num:
    num.remove(2)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print('-'*30)
#lista = []
#for cont in range(0,5):
#    lista.append(int(input('Digite um número: ')))

#for c, v in enumerate(lista):
#    print(f'Encontrei o numero {v} na posição {c}')
#print('Fim')

#criar uma cópia da lista
a = [1 , 3 , 9 , 12]
b = a[:] # isso faz com que só pegue os elementos de dentro da lista
b[2] = 7
print(f'lista A: {a}')
print(f'Lista B: {b}')
