text = input("Ange ett tal: ")
tal = float(text)
if tal >= 1 and tal <= 9:
    print('Talet är ett ental')
elif tal >= 10 and tal <= 99: 
    print('Talet är ett tiotal')
elif tal >= 100 and tal <= 999:
    print('Talet är ett hundratal')
elif tal >= 1000:
    print('Talet är minst ett tusental')
elif tal < 0:
    print('Talet är negativt')
print('klart')