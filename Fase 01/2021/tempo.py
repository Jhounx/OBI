potato = {}

def add_time(time): 
  global potato
  for (key, value) in potato.items():
    if (value["mandou"]):
      value["tempo"] += time

def main():
  global potato
  for i in range(int(input())):
    tipo, value = input().split()
    value = int(value)
    if (tipo == "T"):
      add_time(value)
    elif (tipo == "R"):
      add_time(1)
      if not value in potato:
        potato[value] = {
          "respondeu" : False, 
          "mandou" : True, 
          "tempo" : 0
        }
      else: 
        potato[value]["respondeu"] = False
        potato[value]["mandou"] = True
    elif (tipo == "E"):
      potato[value]["respondeu"] = True
      potato[value]["mandou"] = False
      add_time(1)
    print(potato)

  for (key, value) in potato.items():
    if not(value["respondeu"]):
      print(f"{key} -1")
    else:
      print(f"{key} {value['tempo']}")

if __name__ == "__main__":
  main()