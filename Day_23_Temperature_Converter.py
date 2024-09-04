def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input: Choose conversion type and temperature value
conversion_type = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").upper()
temperature = float(input("Enter the temperature: "))

# Conversion and Output
if conversion_type == 'C':
    print(f"{temperature}°C is equal to {celsius_to_fahrenheit(temperature):.2f}°F")
elif conversion_type == 'F':
    print(f"{temperature}°F is equal to {fahrenheit_to_celsius(temperature):.2f}°C")
else:
    print("Invalid option. Please choose 'C' or 'F'.")
