#https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/chuva/

num_linhas, num_colunas = [int(x) for x in input().split(" ")]

matrix = []
chuva = []
for linha in range(num_linhas):
  a = list(input())
  matrix.append(a)

chuva.append([0, matrix[0].index("o")])
for x, y in chuva: 
  if x == (num_linhas -1): continue
  
  if matrix[x+1][y] == ".":
    matrix[x+1][y] = "o"
    chuva.append([x+1, y])
  else: 
    if (y+1 <= num_colunas-1) and matrix[x][y+1] == ".":
      matrix[x][y+1] = "o"
      chuva.append([x, y+1])
    if (y-1 >= 0) and matrix[x][y-1] == ".":
      matrix[x][y-1] = "o"
      chuva.append([x, y-1])

print("-"*num_colunas)
for linha in matrix:
  print(''.join(linha))