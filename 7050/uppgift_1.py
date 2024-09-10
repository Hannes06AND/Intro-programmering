text = input("Ange ett heltal: ")
tal = int(text)
if tal < 0:
    print('talet är negativt')
else: 
    print('talet är positivt')
print('klart')

text = input("Ange näst sista siffran i ditt personnummer: ")
tal = int(text)
if tal % 2 != 0:
    print('du är kille')
else: 
    print('du är tjej')
print('klart')