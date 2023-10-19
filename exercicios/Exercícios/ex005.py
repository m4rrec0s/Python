n = float(input('Qual é o preço do produto? '))
r = (n - (n * (5/100)))
print('Este é o valor do produto com 5% de Desconto: R${:.2f}'.format(r))

s = float(input('Qual é o valor do seu salário? '))
r2 = (s + (s * (15/100)))
print('''PARABÉNS - você obteve acrescimo de 15% no seu salário

Agora seu salário é de: R${:.2f}'''. format(r2))
