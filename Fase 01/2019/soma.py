#https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/soma/
n, objetivo = [int(x) for x in input().split(" ")]
ar = [int(x) for x in input().split(" ")]
somas_b = 0
for i, value in enumerate(ar): 
  soma = 0 
  for t in range(i, n):
    soma += ar[t]
    if (soma == objetivo):
      somas_b +=1
    elif (soma > objetivo):
      break

print(somas_b)