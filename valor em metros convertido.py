# Solicita ao usuário que ínsira um valor em metros.
metros=float(input(' Digite o valor em metros:'))

#Converte o valor para centimetros e milimetros.
cent=metros*100
milm=metros*1000

#Exibe os resultados
print('O valor de {} metros equivale a {} centimetros e {} milimetros'.format(metros,cent,milm))

