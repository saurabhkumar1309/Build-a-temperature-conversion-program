def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("Choose the unit of your input temperature:")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")
    
    choice = input("Enter 1, 2, or 3: ")
    temp_value = float(input("Enter the temperature value: "))
    
    if choice == "1":
        # Celsius to F and K
        f = celsius_to_fahrenheit(temp_value)
        k = celsius_to_kelvin(temp_value)
        print(f"\n{temp_value}°C is equivalent to:")
        print(f"{f:.2f}°F")
        print(f"{k:.2f}K")
        
    elif choice == "2":
        # Fahrenheit to C and K
        c = fahrenheit_to_celsius(temp_value)
        k = fahrenheit_to_kelvin(temp_value)
        print(f"\n{temp_value}°F is equivalent to:")
        print(f"{c:.2f}°C")
        print(f"{k:.2f}K")
        
    elif choice == "3":
        # Kelvin to C and F
        c = kelvin_to_celsius(temp_value)
        f = kelvin_to_fahrenheit(temp_value)
        print(f"\n{temp_value}K is equivalent to:")
        print(f"{c:.2f}°C")
        print(f"{f:.2f}°F")
        
    else:
        print("Invalid choice. Please restart and choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
