'''Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius'''


cel = 'C'
fa = 'F'
ka = 'K'
escala = input()
t = float(input())

if escala == cel and t>=-273.0:
    print('{:.2f} F'.format(t*9/5 + 32))
    print('{:.2f} K'.format(t + 273.15))
if escala == cel and t < -273.0:
    print('Valor de temperatura abaixo do minimo')

if escala == fa and t>= -459.67:
    print('{:.2f} C'.format((t-32)*(5/9)))
    print('{:.2f} K'.format((t-32)*(5/9)+273.15))
if escala == fa and t< -459.67:
    print('Valor de temperatura abaixo do minimo')

if escala == ka and t >=0.0:
    print('{:.2f} C'.format(t - 273.15))
    print('{:.2f} F'.format((t-273.15)*(9/5)+32))
if escala == ka and t<0.0:
    print('Valor de temperatura abaixo do minimo')
