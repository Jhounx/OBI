#!/usr/bin/env python3

# obi2020 - Ralouim
# r. anido
#

N = int(input())
melhor  = [0]*(N+1)
pmelhor = [0]*(N+1)
pdist = [0]*(N+1)


#adicionando as coordenadas dadas pelo usuario
pontos = [[0, 0]]
for i in range(N):
    x,y = [int(i) for i in input().split()]
    pontos.append([x, y])
    
asd=0
pares = []
teste = {}
for a in range(N+1):
    for b in range(a+1, N+1):
        dx = pontos[a][0] - pontos[b][0]
        dy = pontos[a][1] - pontos[b][1]
        pares.append([dx * dx + dy * dy, a, b]) #adicionando um vertice ao par, dando seu peso e a posição de seus nós
        if not a in teste: 
            teste[a] = []
        if not b in teste:
            teste[b] = []
        teste[b].append(asd)
        teste[a].append(asd)
        asd +=1

atual = 0
num_atual = 1e10
bool_aux = True
contador = 0
print(pares)
while bool_aux: 
    maior = 0
    g = -1 
    for indexCaminho in teste[atual]:
        caminho = pares[indexCaminho]
        if (caminho[0] > maior and caminho[0] < num_atual) and not (contador != 0 and (caminho[1] == 0)): 
            maior = caminho[0]
            g = indexCaminho
    if (g == -1): 
        break
    
    caminhoEscolhido = pares[g]
    print(caminhoEscolhido)
    num_atual = caminhoEscolhido[0]
    atual = caminhoEscolhido[2] if (caminhoEscolhido[1] == atual) else caminhoEscolhido[1]
    
    contador +=1 
    
print(contador)
