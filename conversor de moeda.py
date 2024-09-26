# Considere a taxa de cambio de R$ 5.00 = US$ 1.00
# Solicite ao usuário a quantidade de dinheiro em reais
reais = float(input('Quantos reais você quer converter em dólares? R$'))

#Taxa de cambio
cambio = 5.00

# Calcula a quantidade de dólares
dolares = reais / cambio

# Exibe o resultado
print(f'Com R$ {reais :.2f}, você pode comprar US$ {dolares :.2f}.')

