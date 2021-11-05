'''Escreva um programa que leia os valores (reais) dos raios de dois círculos diferentes e informe qual dos dois possui área maior ou se possuem a mesma área.

Use pi = 3.14'''


raio1 = float(input())
raio2 = float(input())

area1 = 3.14*(raio1**2)
area2 = 3.14*(raio2**2)
if area1 > area2:
    print('Primeiro circulo')
elif area1 < area2:
    print('Segundo circulo')
elif area1 == area2:
    print('Iguais')
