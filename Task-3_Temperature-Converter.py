print("🌡️ Welcome To Temperature Converter!!!!!")
print("Convert  Temperature between Celsius, Fahrenheit, and Kelvin")
print("\n Temperature Conversion Options:")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")
user_choice = input("Enter temperature conversion choice from 1 to 6: ")
temperature_to_convert = float(input("Enter the temperature to convert: "))
if user_choice == '1':
    temperature_result = (temperature_to_convert * 9/5) + 32
    print(f"{temperature_to_convert}°C = {temperature_result:.2f}°F")
elif user_choice == '2':
    temperature_result = temperature_to_convert+ 273.15
    print(f"{temperature_to_convert}°C = {temperature_result:.2f}K")
elif user_choice== '3':
    temperature_result = (temperature_to_convert - 32) * 5/9
    print(f"{temperature_to_convert}°F = {temperature_result:.2f}°C")
elif user_choice == '4':
    temperature_result = (temperature_to_convert - 32) * 5/9 + 273.15
    print(f"{temperature_to_convert}°F = {temperature_result:.2f}K")
elif user_choice == '5':
    temperature_result = temperature_to_convert - 273.15
    print(f"{temperature_to_convert}K = {temperature_result:.2f}°C")
elif user_choice == '6':
    temperature_result = (temperature_to_convert - 273.15) * 9/5 + 32
    print(f"{temperature_to_convert}K = {temperature_result:.2f}°F")
else:
    print("❌ Invalid choice. Please choose a number only from 1 to 6.")
