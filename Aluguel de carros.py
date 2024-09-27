# Escreva um programa que pergunte a quantidade de km percoridos por um carro alugado ,
# e a quantidade de dias pelos quais ele foi alugado .
#Calcule o preço a pagar , sabendo que o carro custa R$ 60 reais po dia e R$ 0.15 por km rodado

# Solicite quantos dias o carro ficou alugado
dias = int ( input ( ' Quantos dias ficou alugado ?'))

# Solicite quantos km foram percorridos
km = float ( input ( ' Quantos km foram percorridos ? '))

# Calcula o pagamento dos dias e km
pago = ( dias * 60) + (km * 0.15)

# Exibe o resultado
print(f' O total a pagar é de R$ : {pago}')

