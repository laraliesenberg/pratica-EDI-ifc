import random
import os

pasta = 'entradas'

def gerar_entrada(arquivo, quantidade, limite=100000):  #limite = k
    numeros = [str(random.randint(0, limite)) for _ in range(quantidade)]
    caminho_arquivo = os.path.join(pasta, arquivo)
    with open(caminho_arquivo, 'w') as f:
        f.write(','.join(numeros))

# Gera 1.000.000 de números entre 0 e 9999

gerar_entrada('entrada10k.txt', 10000)
gerar_entrada('entrada100k.txt', 100000)
gerar_entrada('entrada1m.txt', 1000000)
gerar_entrada('entrada10m.txt', 10000000)
