text1 = input("Ange ett tal: ")
tal1 = float(text1)
text2 = input("Ange ett andra tal: ")
tal2 = float(text2)
text3 = input("Ange ett tredje tal: ")
tal3 = float(text3)
if tal1 < tal2 and tal1 < tal3 and tal2 > tal3:
    print(tal1, tal2, tal3)
elif tal2 < tal1 and tal2 < tal3 and tal1 < tal3:
    print(tal2, tal3, tal1)
elif tal3 < tal1 and tal3 < tal2 and tal2 < tal1:
    print(tal3, tal2, tal1)
elif tal1 < tal2 and tal1 < tal3 and tal2 < tal3:
    print(tal1, tal3, tal2)
elif tal2 < tal1 and tal1 > tal3 and tal3 < tal1:
    print(tal2, tal1, tal3)