# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f =
temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

ask_temperature = input("Would you like to enter in Celsius or Farenheit? (use f for Farenheit or c for Celsius): ").strip().lower()


while ask_temperature not in ['f', 'c']:
    print(ask_temperature)
    ask_temperature = input("Incorrect input. Use f for Farenheit or c for Celsius: ").strip().lower()


def temperature_converter(ask_temperature):
    # Celsius to Fahrenheit (описать докстринг)
    if ask_temperature == 'c':
        Celsius = int(input("Enter a temperature in Celsius: "))
        Fahrenheit = int(Celsius * 1.8) + 32
        print('{}C is {} in Fahrenheit'.format(Celsius, Fahrenheit))
        return Fahrenheit

    if ask_temperature == 'f':
        Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
        Celsius = int((Fahrenheit - 32) * 5.0/9.0)
        print('{}F is {} in Celsius'.format(Fahrenheit, Celsius))
        return Celsius

temperature_converter(ask_temperature)
