frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letra]
print(juntas, ' → ', inverso)
if juntas == inverso:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')
