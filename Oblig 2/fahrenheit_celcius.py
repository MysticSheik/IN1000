temp_f = input("Skriv inn temperatur (fahrentheit): ")
temp_f = float(temp_f)
print("Temperatur (Fahrenheit): " + str(temp_f))

temp_c = (temp_f - 32) * 5/9
print("Temperatur (Celcius): " + str(temp_c))
