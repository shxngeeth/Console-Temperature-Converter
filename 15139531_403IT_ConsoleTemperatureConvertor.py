def diplaymenu():
    print('\n15139531-TEMPERATURE CONVERTOR\n1. Celsius to Fahrenheit \n2. Celsius to Kelvin \n3. Fahrenheit to Celsius\n4. Fahrenheit to Kelvin\n5. Kelvin to Celsius\n6. Kelvin to Fahrenheit')

while True:
    try:
        diplaymenu()
        choice = input('\nEnter choice (1-6) : ')

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print('Invalid Choice: Enter number between 1 to 6 : ')
            continue

        temp = float(input('Enter temperature : '))
        if choice == '1':
            print(f'{temp}°C = {(temp * 9 / 5) + 32}°F')
        elif choice == '2':
            print(f'{temp}°C = {temp + 273.15}°K')
        elif choice == '3':
            print(f'{temp}°F = {(temp - 32) * 5 / 9}°C')
        elif choice == '4':
            print(f'{temp}°F = {(temp - 32) * 5 / 9 + 273.15}°K')
        elif choice == '5':
            print(f'{temp}K = {temp - 273.15}°C')
        elif choice == '6':
            print(f'{temp}K = {(temp - 273.15) * 9 / 5 + 32}°F')

        c = input('Press t to terminate : ')
        if c == 't':
            print('Temperature Convertor exiting...')
            break
    except ValueError:
        print('Invalid input! Please enter a valid numeric temperature')
