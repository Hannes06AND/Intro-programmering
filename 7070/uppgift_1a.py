import random
fraga = input("Vill du spela? j/n: ")
tarning1 = random.randint(1, 6)
tarning2 = random.randint(1, 6)
if fraga == "j":
    print(tarning1)
    print(tarning2)
if tarning1 == tarning2:
    print('vinst')
elif tarning1 != tarning2: 
    print('förlust')
if fraga == "n":
    print('Vad roligt att du spelade en stund!')