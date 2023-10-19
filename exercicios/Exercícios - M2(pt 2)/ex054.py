import tkinter as tk

def sacar():
    cinquenta_reais = vinte_reais = dez_reais = um_real = 0

    valor = int(valor_entry.get())

    while True:
        if valor >= 50:
            valor -= 50
            cinquenta_reais += 1
        elif valor < 50 and valor >= 20:
            valor -= 20
            vinte_reais += 1
        elif valor < 20 and valor >= 10:
            valor -= 10
            dez_reais += 1
        elif valor <10 and valor > 0:
            valor -= 1
            um_real += 1
        elif valor == 0:
            break

    output_text = f'''TOTAL DE CÉDULAS
{'-'*40}
'''

    if cinquenta_reais > 0:
        output_text += f'{cinquenta_reais} NOTAS DE R$ 50.00\n'
    if vinte_reais > 0:
        output_text += f'{vinte_reais} NOTAS DE R$ 20.00\n'
    if dez_reais > 0:
        output_text += f'{dez_reais} NOTAS DE R$ 10.00\n'
    if um_real > 0:
        output_text += f'{um_real} NOTAS DE R$ 1.00\n'
    output_label.config(text=output_text)

root = tk.Tk()
root.title('CAIXA ELETRÔNICO')

valor_label = tk.Label(root, text='Quanto você quer sacar?')
valor_label.pack()

valor_entry = tk.Entry(root)
valor_entry.pack()

sacar_button = tk.Button(root, text='Sacar', command=sacar)
sacar_button.pack()

output_label = tk.Label(root, text='', font=('Arial', 12))
output_label.pack()

root.mainloop()
