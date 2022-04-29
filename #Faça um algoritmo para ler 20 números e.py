#Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos
# 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa
import random
lista1 = []
for numero in range(20):
    numero = random.randint(0,1000)
    lista1.append(numero)
print(lista1)
print(lista1.reverse())

    