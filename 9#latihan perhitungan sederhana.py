#latihan  komversi satuan temperature

#program konversi celsius kesatuan lain

# Celcius

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celsius = float(input("Masukkan Suhu Dalam Celsius:"))
print("Suhu Adalah:",celsius)

# Reamur
reamur = (4 / 5) * celsius
print("Suhu Dalam Reamur Adalah:",reamur,"Reamur")

#Fahrenheit
fahrenheit = ((9 / 5) * celsius) + 32
print("Suhu Dalam Fahrenheit Adalah:",fahrenheit,"Fahrenheit")

#Kelvin
kelvin = celsius + 273
print("Suhu Dalam Kelvin Adalah:",kelvin,"Kelvin")
