import random
fraga = input("Vill du spela? j/n: ")
tarning1 = random.randrange(1, 6)
tarning2 = random.randrange(1, 6)
if fraga == "j":
    print(tarning1)
    print(tarning2)
if tarning1 == tarning2:
    print('vinst')
else: 
    print('förlust')