#Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no 
# vetor VET e em que posições se encontram.

import random
numero_vet = []
vet = []
for numero in range(1,51):
    vet.append(random.randint(1,10))
print(vet)
for g in vet:
    if g not in numero_vet:
        indices = [indice for indice, valor in enumerate(vet) if valor == g]
        print("numero:",g,"posição:",indices)
        numero_vet.append(g)
