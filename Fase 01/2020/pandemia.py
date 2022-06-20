#https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/pandemia/

_, totalDias = map(int, input().split(" "))
amigo, reuniao = input().split(" ")

infectados = [amigo]
for i in range(totalDias):
  ar = input()
  if (i >= (int(reuniao) -1)):
    ar = ar.split(" ")[1::]
    for infectado in infectados:
      if infectado in ar: 
        for j in ar: 
          if not j in infectados:
            infectados.append(j)

print(len(infectados))