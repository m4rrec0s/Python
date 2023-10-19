n = str(input('digite uma frase: ')).strip().upper()

print('sua frase tem {} letras A.' .format(n.count('A')))
print('A primeira letra A apareceu na posição {}'.format(n.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(n.rfind('A')+1))

print('=='*20)

n1 = str(input('Digite seu nome completo: ')).strip()
d = (n1.split())
s1 = (d[0])
s2 = (d[len(d)-1])
print('Muito prazer, {} {}.'.format(s1 , s2))
