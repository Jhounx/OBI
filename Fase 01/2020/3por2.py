#https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/3por2/
precos = [ ]

for i in range(int(input())):
  p = int(input())
  precos.append(p)

precos.sort(reverse=True)

soma = 0 
for index, num in enumerate(precos, start=1):
  if (index %3 != 0):
    soma += num

print(soma)


