def kelvintocelsius(kelvin):
    answer = kelvin - 273.15
    return answer
temp = float(input("Ange temperatur i grader Kelvin: "))
print("Temperaturen är", kelvintocelsius(temp), "Celsius")