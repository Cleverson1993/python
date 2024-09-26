#Solicite o salário atual do funcionário
salario_atual = float(input(' Digite o salário atual do funcionário:'))

#Calcula o aumento de 15%
aumento = salario_atual * 0.15

# Calcula o novo salário
novo_salario = salario_atual + aumento

# Exibe o novo salário
print(f'O seu novo salário com 15% de aumento é : R${novo_salario:.2f}')