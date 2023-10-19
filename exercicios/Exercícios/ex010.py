n = int(input('Digite um numero entre 0 e 9999: '))

milhar, resto = divmod(n, 1000)
centena, resto = divmod(resto, 100)
dezena, unidade = divmod(resto, 10)

print(f"Milhar: {milhar}, Centena: {centena}, Dezena: {dezena}, Unidade: {unidade}")

#dizer se tem SANTO, sim ou não

c = str('Qual é o nome da sua cidade? ')
c1 = (c.split(c.find('SANTO')))
print(c1[0])