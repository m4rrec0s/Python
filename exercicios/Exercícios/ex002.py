n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ((n1 + n2)/2)
print('='*30)
print('A média do anulo é: {}'.format(m))
print('='*30)

n3 = int(input('Digite um vamor em Metros: '))
cm = (n3 * 100)
mm = (n3 * 1000)
print('''
{} metros
- em centimetros: {}
- em milimetros: {}'''.format(n3, cm, mm))
