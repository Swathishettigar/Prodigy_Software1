# Temperature Conversion Program

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print(f"Celsius: {temp} °C")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Kelvin: {kelvin:.2f} K")

elif unit == "F":
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"Fahrenheit: {temp} °F")
    print(f"Celsius: {celsius:.2f} °C")
    print(f"Kelvin: {kelvin:.2f} K")

elif unit == "K":
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"Kelvin: {temp} K")
    print(f"Celsius: {celsius:.2f} °C")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")

else:
    print("Invalid unit! Please enter C, F, or K.")
