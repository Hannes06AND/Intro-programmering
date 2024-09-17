text = input("Ange ett tal: ")
tal = float(text)
if tal >= 1 and tal <= 9:
    print('Talet är ensiffrigt')
elif tal >= 10 and tal <= 99: 
    print('Talet är tvåsiffrigt')
elif tal >= 100 and tal <= 999:
    print('Talet är tresiffrigt')
elif tal >= 1000:
    print('Talet är minst fyrsiffrigt')
elif tal < 0:
    print('Talet är negativt')
print('klart')