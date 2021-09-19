import time
import random

random.seed(42)

sorteio_tamanho_vetor = random.randrange(1000,10000)
print("Tamanho do vetor: ", sorteio_tamanho_vetor)

A = [random.randint(0,1000) for i in range(sorteio_tamanho_vetor)]
n = len(A)
x = 5

def busca_linear(A, n, x):
    resposta = -1
    for i in range(0, n):
        if(A[i] == x): resposta = i
    return resposta

def busca_lienar_melhorada(A, n, x):
    resposta = -1
    for i in range(0, n):
        if (A[i == x]):
            resposta = i
            break
    return resposta

busca_lienar_melhorada(A, n, x)