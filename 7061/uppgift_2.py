svar = input("Gissa mitt tal: ")
tal = int(svar)
while svar > "42":
    print('för litet ')
    svar = input("Gissa mitt tal: ")
while svar < "42":
    print('för stort')
print('Du gissade rätt ')