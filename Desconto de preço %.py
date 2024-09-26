# Solicita o preço do produto ao usuário.
preco = float( input( ' digite o preço do produto :R$'))

# Calcula o desconto.
desconto = preco * 0.05

# Calcula o novo preço com desconto aplicado
novo_preco = preco - desconto

# Exibe o resultado
print(f'O novo preço do produto com 5% de desconto é : R$ {novo_preco}')




