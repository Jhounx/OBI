#https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/imperial/

dic = { }

max = int(input())
ultimo_marcado = -1  
for i in range(max):
  num = int(input())
  if not num in dic: 
    dic[num] = 1
  else: 
    if not (ultimo_marcado == num):
      ultimo_marcado = num 
      dic[num] +=1 
      
print(dic)
asd = [x for x in dic.values()]
asd.sort(reverse=True)
print(asd)
soma = asd[0]
if (len(asd) > 1): 
  soma += asd[1]
print(soma)