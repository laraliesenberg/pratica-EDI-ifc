import time
import os
import psutil

#dados: lista que será ordenada
#esquerda: índice inicial da lista/sublista a ordenar
#direita: índice final da lista/sublista a ordenar
def quicksort_threeway(dados, esquerda, direita):
    if esquerda >= direita:
        return

    esquerdaIndice = esquerda       # Índice da parte < pivô
    direitaIndice = direita         # Índice da parte > pivô
    pivo = dados[esquerdaIndice]    # Define o pivô como primeiro elemento 
    loopIndice = esquerda           # Índice atual no laço

    while loopIndice <= direitaIndice:
        if dados[loopIndice] < pivo:
            dados[esquerdaIndice], dados[loopIndice] = dados[loopIndice], dados[esquerdaIndice]
            esquerdaIndice += 1
            loopIndice += 1
        elif dados[loopIndice] > pivo:
            dados[loopIndice], dados[direitaIndice] = dados[direitaIndice], dados[loopIndice]
            direitaIndice -= 1
        else:
            loopIndice += 1

    # Chamada recursiva nas partições: menor e maior que o pivô
    quicksort_threeway(dados, esquerda, esquerdaIndice - 1)     # Menores que o pivô
    quicksort_threeway(dados, direitaIndice + 1, direita)       # Maiores que o pivô

def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
        numeros = [int(x.strip()) for x in conteudo.split(',') if x.strip().isdigit()]
        return numeros

def salvar_numeros_em_arquivo(nome_arquivo, numeros):
    with open(nome_arquivo, 'w') as f:
        f.write(', '.join(str(num) for num in numeros))

def obter_memoria_usada():
    processo = psutil.Process(os.getpid())
    memoria = processo.memory_info().rss / 1024 / 1024  # Em MB
    return round(memoria, 4)


if __name__ == "__main__":
    pasta_entradas = "entradas"
    pasta_saidas = "saidas"
    entradas = ["entrada10k.txt", "entrada100k.txt", "entrada1m.txt", "entrada10m.txt"]
    saidas = ["quick10k.txt", "quick100k.txt", "quick1m.txt", "quick10m.txt"]

    for i, entrada in enumerate(entradas):
        caminho_arquivo = os.path.join(pasta_entradas, entrada)
        tempo_inicio = (time.process_time_ns() if i==0 else time.process_time())
        memoria_inicio = obter_memoria_usada()
        saida = saidas[i]
        caminho_saida = os.path.join(pasta_saidas, saida)

        dados = ler_numeros_do_arquivo(caminho_arquivo)

        quicksort_threeway(dados, 0, len(dados) - 1)

        salvar_numeros_em_arquivo(caminho_saida, dados)

        tempo_fim = (time.process_time_ns() if i==0 else time.process_time())
        memoria_fim = obter_memoria_usada()

        tempo_total = round(tempo_fim - tempo_inicio, 6)
        memoria_usada = round(memoria_fim - memoria_inicio, 6)
    
        print(f"Números ordenados foram salvos em '{saida}'")
        if i == 0:
            print(f"Tempo de execução: {tempo_total} nano segundos")
        else:
            print(f"Tempo de execução: {tempo_total} segundos")
        print(f"Memória usada: {memoria_usada} MB", end="\n\n")