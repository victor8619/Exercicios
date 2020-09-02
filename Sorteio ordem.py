import random
aluno1 = str(input('\033[4;36mDigite o nome do 1° aluno:\033[m '))
aluno2 = str(input('\033[4;35mDigite o nome do 2° aluno:\033[m '))
aluno3 = str(input('\033[4;34mDigite o nome do 3° aluno:\033[m '))
aluno4 = str(input('\033[4;33mDigite o nome do 4° aluno:\033[m '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem de apresentação será\n{lista}')
