num_cheques, num_pessoas = [int(x) for x in input().split()]
data = {}

for x in range(num_cheques):
  cheque_data = [int(x) for x in input().split()]
  if not cheque_data[0] in data:
    data[cheque_data[0]] = 0
  if not cheque_data[2] in data: 
    data[cheque_data[2]] = 0
  data[cheque_data[0]] -= cheque_data[1]
  data[cheque_data[2]] += cheque_data[1]

print(data)