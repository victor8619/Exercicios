import random
aluno1 = str(input('Digite o nome do 1° aluno: '))
aluno2 = str(input('Digite o nome do 2° aluno: '))
aluno3 = str(input('Digite o nome do 3° aluno: '))
aluno4 = str(input('Digite o nome do 4° aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
