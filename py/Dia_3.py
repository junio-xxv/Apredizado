import random


nomes = []

for i in range(3):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)
    
print('sorteio de numeros')
for nome in nomes:
    num = random.randint(1, 100)
    print(f"nome: {nome}  numero: ",num)
        