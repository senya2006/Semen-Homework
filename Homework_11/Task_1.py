def celsius_to_fahrenheit(celsius: float):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float):
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature: float, unit: str):
    try:
        if unit.upper() == 'C':
            return celsius_to_fahrenheit(temperature)
        elif unit.upper() == 'F':
            return fahrenheit_to_celsius(temperature)
        else:
            raise ValueError("Error. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        return str(e)

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

converted_temperature = convert_temperature(temperature, unit)
print(f"The converted temperature from temperature: {temperature} and unit: {unit} is: {converted_temperature}")
