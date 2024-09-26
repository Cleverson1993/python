# Solicita as dimensões da parede ao usuário.
largura = float(input('Digite a largura da parede em metros :'))

altura = float(input('Digite a altura da parede em metros'))

#Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária.
litros_tinta = area / 2

# Exibe os resultados.
print(f'A área da parede e de : {area} metros quadrados' )
print(f' Você precisará de {litros_tinta} litors de tinta para pintar a parede')

