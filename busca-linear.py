import time
import random

random.seed(1000)

sorteio_tamanho_vetor = random.randrange(1000000,10000000)
print("\nTamanho do vetor: ", sorteio_tamanho_vetor)
print("=================================")

A = [random.randint(0,1000) for i in range(sorteio_tamanho_vetor)]
n = len(A)
x = 1000

def busca_linear(A, n, x):
    resposta = -1
    for i in range(0, n):
        if(A[i] == x): 
            resposta = i
    return resposta

def busca_linear_melhorada(A, n, x):
    resposta = -1

    for i in range(0, n):
        if (A[i] == x):
            resposta = i
            break

    return resposta

def busca_linear_sentinela(A, n, x):
    resposta = -1
    
    ultimo = A[n - 1]
    A[n - 1] = x
    i = 0

    while (A[i] != x):
        i += 1
    
    A[n - 1] = ultimo

    if ((i < n - 1) or (A[n - 1] == x)):
        resposta = i
    
    return resposta

#Chamando as funções definidas

#Busca Linear
inicia_tempo = time.time_ns()
saida = busca_linear(A, n, x)
termina_tempo = time.time_ns()
tempo = termina_tempo - inicia_tempo
print("\nBusca Linear")
print("Resposta = ", saida, " em ", tempo, "ns.\n")

#Busca Linear Melhorada
inicia_tempo = time.time_ns()
saida = busca_linear_melhorada(A, n, x)
termina_tempo = time.time_ns()
tempo = termina_tempo - inicia_tempo
print("\nBusca Linear Melhorada")
print("Resposta = ", saida, " em ", tempo, "ns.\n")

#Busca Linear com Sentinela
inicia_tempo = time.time_ns()
saida = busca_linear_sentinela(A, n, x)
termina_tempo = time.time_ns()
tempo = termina_tempo - inicia_tempo
print("\nBusca Linear com Sentinela")
print("Resposta = ", saida, " em ", tempo, "ns.\n")


