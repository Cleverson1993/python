######Lendo um número real do teclado

#numero = float(input('Digite um número real: '))

##### Mostrando a porção inteira do número

#print(f'O valor digitado foi {numero} e a sua porção inteira é {int(numero)}.')
###########################################################################################################


#existe tambem este outro modo
# Importando a função trunc do módulo math
from math import trunc

# Lendo um número real do teclado
numero = float(input("Digite um número real: "))

# Mostrando a porção inteira do número
print(f"O valor digitado foi {numero} e a sua porção inteira é {trunc(numero)}.")
