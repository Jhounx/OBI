#nao precisa de um contador, so precisa comparar o numero final de numeros com o inicial ai vc vai saber quantos numeros foram tirados 
#https://olimpiada.ic.unicamp.br/pratique/p2/2021/f2/lista/
from copy import copy

qtd = int(input())
nums = [int(x) for x in input().split(" ")]
combs = [nums]
palinds = [ ]

def is_palindrome(lista): 
    qt = len(lista) //2 
    l1 = lista[0:qt]
    l2 = lista[::-1][0:qt]
    return (l1 == l2)

if (is_palindrome(nums)):
    print(0)
    exit()

for comb in combs: 
    for i in range(len(comb)-1):
        old_aux = copy(comb)
        num = old_aux[i]
        num_1 = old_aux[i+1]
        old_aux[i] = num + num_1
        del old_aux[i+1]
        if (is_palindrome(old_aux)):
            palinds.append(qtd - len(old_aux))
            continue
        if (len(old_aux) == 2):
            continue
        combs.append(old_aux)

palinds.sort()
print(palinds[0])
    
