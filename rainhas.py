import math
import random
import time
from copy import deepcopy #copia pra n alterar o objeto 
from random import randint

global N 
N = 8
R = 'R'
exito = 0
tempo_sucesso = []
tempo_falha = []
temp = []
i = 0

def cria_tabuleiro():
    #Cria o tabuleiro sem rainhas
    tabuleiro = []
    for i in range(0, N):
        tabuleiro.append(['0'] * N)
    return tabuleiro

def aloca_rainha(tabuleiro):
    #Coloca a rainha aleatoriamente utilizando range
    for i in range(0, N):
        tabuleiro[randint(0, N - 1)][i] = 'R'
    return tabuleiro

def print_tabuleiro(tabuleiro=[]):
    for linha in tabuleiro:
        print(' '.join(linha))

def calcula_ataques(posicao_tab, i, j):
    #calcula os ataques da rainha incrementando cada numero de ataque
    num_ataques = 0
    k = 1
    j += k
    
    while j < N:
        if posicao_tab[i][j] == R:
            num_ataques += 1
        if i + k < N and posicao_tab[i + k][j] == R:
            num_ataques += 1
        if i - k > -1 and posicao_tab[i - k][j] == R:
            num_ataques += 1
        k += 1
        j += 1
        
    print("Ataques : ", num_ataques)
    print()
    return num_ataques
    
def pega_posicao(v, valor, coluna):
    y = -1
    x = -1
    for i in range(N):
        #Encontra o índice de valor no vetor
        if v[i][coluna] == valor:
            x = i
            y = coluna
            break
    return x, y
  
def calculo_heuristico(posicao_tab):
    valor_heuristica = 0

    for j in range(N):
        for i in range(N):
            if posicao_tab[i][j] == R:
                valor_heuristica += (calcula_ataques(posicao_tab, i, j))
    return valor_heuristica

def gen_vizinho(posicao_tab):
  
    tabela_heuristica = [[0] * N for i in range(N)]

    for j in range(N):
        x, y = pega_posicao(posicao_tab, R, j)
    for i in range(N):
            if x == i and y == j:
                tabela_heuristica[i][j] = float('inf')
            else:
                vizinho = deepcopy(posicao_tab)
                vizinho[i][j], vizinho[x][y] = vizinho[x][y], vizinho[i][j]
                tabela_heuristica[i][j] = calculo_heuristico(vizinho)
    return tabela_heuristica

def performance_tempera(posicao_atual, heuristico_novo):
    global exito
    temperatura = 100
    verifica_exito = False
    caminho = []
    tempo_inicio = time.time()

    if heuristico_novo == 0:
        print("Já resolvido!\n")
    else:
        while temperatura > 1:
            temperatura = temperatura - 0.5
            print("Temperatura : ", temperatura)
            temp.append(temperatura)
            print()
            print_tabuleiro(posicao_atual)
            print("\n================================\n")

            tabela_heuristica = []
          
            vizinho, heuristico_vizinho = sucessor(posicao_atual, caminho)

            if heuristico_vizinho > heuristico_novo:
                diff = heuristico_vizinho - heuristico_novo
                prob = float(float(math.e) ** float(float(-diff) / float(temperatura)))
              
                if prob > random.uniform(0, 1):
                    posicao_atual = vizinho
                    heuristico_novo = heuristico_vizinho
                    caminho.pop()
              
            else:
                posicao_atual = vizinho
                heuristico_novo = heuristico_vizinho
                if heuristico_vizinho == 0:
                    print("\nResultado:")
                    print_tabuleiro(posicao_atual)
                    print()
                    verifica_exito = True
                    break
              
        if verifica_exito:
          print("Solução encontrada!!\n")
          exito += 1
          tempo_sucesso.append(time.time() - tempo_inicio)
          print("Temperatura : ", temperatura)
          print("Tempo : ", time.time() - tempo_inicio)
          
        else: 
          print("Solução não encontrada!!\n")
          tempo_falha.append(time.time() - tempo_inicio)
          print("Temperatura : ", temperatura)
          print("Time : ", time.time() - tempo_inicio)
        
    return caminho

def sucessor(posicao_atual, caminho):
    i, j = 0, 0
    for r in range(10):
        i = randint(0, N - 1)
        j = randint(0, N - 1)
        if posicao_atual[i][j] != R:
            break

    x, y = pega_posicao(posicao_atual, R, j)
    vizinho = deepcopy(posicao_atual)
    vizinho[i][j], vizinho[x][y] = vizinho[x][y], vizinho[i][j]
    heuristico_vizinho = calculo_heuristico(vizinho)
    caminho.append([(x, y), (i, j)])
    return vizinho, heuristico_vizinho
    #guardando as coordenadas do caminho para chegar no inicio
  
def main():
    print("\nTabuleiro inicial:")

    tabuleiro = cria_tabuleiro()
    init_pos = aloca_rainha(tabuleiro)

    posicao_atual = deepcopy(init_pos)
    print_tabuleiro(posicao_atual)
    print("\n================================")
    
    heuristico_novo = calculo_heuristico(posicao_atual)
    Aux = performance_tempera(posicao_atual, heuristico_novo)
      
main()