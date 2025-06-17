import random

a = random.randint(1, 10)
b = 0
tentativas = 0

while b != a:
    b = int(input("escolha um numero de 1 ou 10: "))
    tentativas += 1 

if b != a:
    print('vc perdeu!')
else:
    print('vc ganhou! tentativas:', tentativas  )
    


