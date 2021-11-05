'''Faça um programa que calcule a área da superfície e o volume de um cilindro. Use pi = 3.14.

O valor de saída deve ser arredondado usando 2 casas decimais.'''


altura = float(input())
raio = float(input())
area = (2 * 3.14 * raio ** 2) + (2 * 3.14 * raio * altura)
vol = 3.14 * raio ** 2 * altura
print('{:.2f}\n{:.2f}'.format(vol,area))
