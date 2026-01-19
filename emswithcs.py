import psutil
import time
import os

def counting_sort(lista):
    k = max(lista)
    contagem = [0]*(k+1)
    for i in lista:
        contagem[i] += 1
    listaOrdenada = []
    for valor, frequencia in enumerate(contagem):
        listaOrdenada.extend([valor]*frequencia)
    return listaOrdenada

def divide_in_chunks(arquivo, tamanho, tamanho_entrada):
    blocos = []
    with open(arquivo, 'r') as arq:
        dados = arq.read().strip()
        numeros = list(map(int, dados.split(',')))
        for i in range(0, len(numeros), tamanho):
            bloco = numeros[i:i+tamanho]
            listaOrdenada = counting_sort(bloco)
            nome = "bloco" + tamanho_entrada + str(len(blocos)) + ".txt"
            saida = os.path.join("blocos", nome)
            with open(saida, 'w') as b:
                b.write(','.join(map(str, listaOrdenada)))
            blocos.append(saida)
    return blocos

def merge_two_lists(a, b):
    i = 0
    j = 0
    lista_ordenada = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            lista_ordenada.append(a[i])
            i += 1
        else:
            lista_ordenada.append(b[j])
            j += 1
    lista_ordenada.extend(a[i:])
    lista_ordenada.extend(b[j:])
    return lista_ordenada
        

def merge_chuncks(blocos, saida):
    arquivos = [open(b, 'r') for b in blocos]
    listas = []

    for arq in arquivos:
        dados = arq.read().strip()
        if dados:
            numeros = list(map(int, dados.split(',')))
        else:
            numeros = []
        listas.append(numeros)
        arq.close()

    while len(listas) > 1:
        a = listas.pop(0)
        b = listas.pop(0)
        listas.append(merge_two_lists(a, b))

    lista_final = listas[0]

    with open(saida, "w") as resultado:
        resultado.write(','.join(map(str, lista_final)))

    return saida

def obter_memoria_usada():
    processo = psutil.Process(os.getpid())
    memoria = processo.memory_info().rss / 1024 / 1024  # Em MB
    return round(memoria, 4)


if __name__ == "__main__":
    pasta_entradas = "entradas"
    pasta_saidas = "saidas"
    entradas = ["entrada10k.txt", "entrada100k.txt", "entrada1m.txt", "entrada10m.txt"]
    saidas = ["ems10k.txt", "ems100k.txt", "ems1m.txt", "ems10m.txt"]
    tamanhos_arquivos = ["10k", "100k", "1m", "10m"]
    tamanho_blocos = [5000, 50000, 100000, 100000]
    

    for i, entrada in enumerate(entradas):
        caminho_arquivo = os.path.join(pasta_entradas, entrada)
        caminho_saida = os.path.join(pasta_saidas, saidas[i])
        tempo_inicio = time.process_time()
        memoria_inicio = obter_memoria_usada()

        merge_chuncks(divide_in_chunks(caminho_arquivo, tamanho_blocos[i], tamanhos_arquivos[i]), caminho_saida)

        tempo_fim = time.process_time()
        memoria_fim = obter_memoria_usada()

        tempo_total = round(tempo_fim - tempo_inicio, 6)
        memoria_usada = round(memoria_fim - memoria_inicio, 6)

        print(f"Números ordenados foram salvos em '{saidas[i]}'")
        print(f"Tempo de execução: {tempo_total} segundos")
        print(f"Memória usada: {memoria_usada} MB", end= "\n\n")