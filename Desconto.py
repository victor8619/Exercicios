prod = float(input('Qual o preço do produto em reais?'))
desc = prod * 5 / 100
prod2 = prod - desc
print(f'O produto custava {prod:.2f} reais e agora,\n com desconto de 5%, custa {prod2:.2f} reais.')

