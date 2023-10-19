from tabulate import tabulate

lista = ('Arroz',5.99, 'Feijão',7.99,'Café em pó',8.99,'Leite em pó',9.99,
         'Farinha de trigo',3.49,'Farinha de mandioca',2.99,'Fubá de milho',2.49,
         'Creme dental',2.99,'Sabonete líquido',5.49,'Shampoo', 7.99,'Condicionador',8.99,
         'Desodorante aerosol',9.99,'Papel higiênico',11.99,'Detergente líquido',4.49,
         'Amaciante de roupas',6.49,'Água sanitária',2.49)

table = []
p = 0
r = 1
while p < len(lista):
    table.append([lista[p], f'R$ {lista[r]:>6}'])
    p += 2
    r += 2

headers = ['Produto', 'Preço']
table_str = tabulate(table, headers, tablefmt='fancy_grid')
print(table_str)
