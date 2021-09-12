escala_inicial = str(input('Digite a escala inicial: ')).upper()
escala_final = str(input('Digite a escala final: ')).upper()
temp_inicial = float(input('Digite a temperatura inicial: '))
kelvin_to_celsius = lambda x: x - 273.15;
kelvin_to_fahrenheit = lambda x: (x - 273.15) * 9/5 + 32;
fahrenheit_to_kelvin = lambda x: (x - 32) * 5/9 + 273.15
fahrenheit_to_celsius = lambda x: (x -32) * 5/9
celsius_to_kelvin = lambda x: x + 273.15
celsius_to_fahrenheit = lambda x: (x * 9/5) + 32
if escala_inicial == 'C' and escala_final == 'F': temp_final = celsius_to_fahrenheit(temp_inicial); print(f'{temp_inicial} °{escala_inicial} em Fahrenheit: {temp_final} °{escala_final}')
if escala_inicial == 'C' and escala_final == 'K': temp_final = celsius_to_kelvin(temp_inicial); print(f'{temp_inicial} °{escala_inicial} em Kelvin: {temp_final} {escala_final}')
if escala_inicial == 'F' and escala_final == 'C': temp_final = fahrenheit_to_celsius(temp_inicial); print(f'{temp_inicial} °{escala_inicial} em Celsius: {temp_final} °{escala_final}')
if escala_inicial == 'F' and escala_final == 'K': temp_final = fahrenheit_to_kelvin(temp_inicial); print(f'{temp_inicial} °{escala_inicial} em Kelvin: {temp_final} {escala_final}')
if escala_inicial == 'K' and escala_final == 'C': temp_final = kelvin_to_celsius(temp_inicial); print(f'{temp_inicial} {escala_inicial} em Celsius: {temp_final} °{escala_final}')
if escala_inicial == 'K' and escala_final == 'F': temp_final = kelvin_to_fahrenheit(temp_inicial); print(f'{temp_inicial} {escala_inicial} em Celsius: {temp_final} °{escala_final}')
