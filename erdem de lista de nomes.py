import random

n1 = str(input(' primeiro aluno: '))
n2 = str(input(' segundo aluno: '))
n3 = str(input(' terceiro aluno: '))
n4 = str(input(' quarto aluno: '))
n5 = str(input(' quinto aluno: '))
n6 = str(input(' sexto aluno: '))
n7 = str(input(' sétimo aluno: '))
lista = [n1,n2,n3,n4,n5,n6,n7]
random.shuffle(lista)
print(f' A ordem de apresentação será')
print(f' {lista}')

