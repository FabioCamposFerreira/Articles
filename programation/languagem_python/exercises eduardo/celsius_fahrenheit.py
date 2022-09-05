def celsius_fahrenheit(celsius):
    #f = c*(9/5)+32
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
def fahrenheit_celsius(fahrenheit):
    #c = (f - 32)*(5/9)
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
scale = input('Converter para celsius ou para fahrenheit:')
if scale == 'celsius' or scale == 'fahrenheit': 
    value = int (input('Qual o valor:'))
    if scale == 'celsius':
        print (value, 'fahrenheit equilave a', fahrenheit_celsius(value), 'celsius')
    if scale == 'fahrenheit':
        print (value, 'celsius equilave a', celsius_fahrenheit(value), 'fahrenheit')
else: print ('Escala invalida!')
