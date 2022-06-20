#https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/promocao/

num_cidades = int(input())

cidades = [{}, {}]
for _ in range(num_cidades -1): 
  ar = [int(x) for x in input().split(" ")]
  cidades[ar[2]][ar[1]] = ar[0]

ar = []
for i in range(num_cidades):
  contador = 1
  a = i
  alternador = 0 if a in cidades[0] else 1
  while (True):
    contador += 1
    try:
      a = cidades[alternador][a]
    except: 
      break
    alternador = 0 if alternador == 1 else 1

  ar.append(contador)

print(max(ar))
