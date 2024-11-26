import random
tarning = []
for i in range(33):
    tarning.append(random.randint(1,3))
antaltreor = 0
for i in tarning:
    if i == 3:
        antaltreor = antaltreor + 1
print("Antal treor:",antaltreor)