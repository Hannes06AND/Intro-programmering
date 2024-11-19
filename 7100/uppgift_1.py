import random
tarningskast = []
for i in range(10):
    tarningskast.append(random.randint(1, 6)) 
tarningskast.sort()
summan = sum(tarningskast)
medelvarde = summan / len(tarningskast)
minsta = min(tarningskast)
storsta = max(tarningskast)
antal_sexor = tarningskast.count(6)
print("Tärningskast: ", tarningskast)
print("Total summa: ", summan)
print("Medelvärde: ", medelvarde)
print("Minsta värde: ", minsta)
print("Största värde: ", storsta)
print("Antal sexor: ", antal_sexor)