# Tuplas () são imutáveis
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu comi {cont + 1} - {lanche[cont]}')

print('=' * 20)

for cont in lanche:
    print(f'Eu comi {cont}')

print('=' * 20)

for pos, comida in enumerate(lanche):
    print(f'Eu comi {pos + 1} - {comida}')
