text1 = input("Ange ett tal: ")
tal1 = float(text1)
text2 = input("Ange ett andra tal: ")
tal2 = float(text2)
text3 = input("Ange ett tredje tal: ")
tal3 = float(text3)
if tal1 < tal2 and tal3 > tal1:
    print('Det första talet är minst')
elif tal1 > tal2 and tal3 > tal2:
    print('Det andra talet är minst')
elif tal1 > tal3 and tal2 > tal3:
    print('Det tredje talet är minst')