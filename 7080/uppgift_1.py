def kelvintocelsius(kelvin):
    return kelvin - 273.15
temp = float(input("Ange temperatur i grader Kelvin: "))
print("Temperaturen är", kelvintocelsius(temp), "Celsius")