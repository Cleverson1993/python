# Solicita ao usuário que digite um número inteiro
n=int(input('Digite um número inteiro :'))

#Exibe a tábuada do número
print('Tábuada do {} é'.format(n))
for i in range(1,11):
    print('{} x {} = {}'.format(n,i,n*i))
