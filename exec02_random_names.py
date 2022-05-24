import random
lista_nomes = []

nomes = input('Digite o 1° nome:  ')
lista_nomes.append({'nomes':nomes})

nomes = input('Digite o 1° nome:  ')
lista_nomes.append({'nomes':nomes})

nomes = input('Digite o 1° nome:  ')
lista_nomes.append({'nomes':nomes})

nomes = input('Digite o 1° nome:  ')
lista_nomes.append({'nomes':nomes})

nrandom = random.choice(lista_nomes)
print(f'Os nomes digitados foram {nrandom}!')