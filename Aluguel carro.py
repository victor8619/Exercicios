dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você rodou? '))
print('Com essas condiçoes: ')
print(f'Você ficou com o carro {dia} dias e rodou {km:.2f} Km')
valordia = dia * 60
valorkm = km * 0.15
print(f'Com isso, o valor a pagar é de R$ {valorkm + valordia:.2f}')
