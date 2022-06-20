#https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/idade/

monica = int(input())

ar = [int(input()) for _ in range(2)]
ar.append(monica - (ar[0] + ar[1]))
print(max(ar))