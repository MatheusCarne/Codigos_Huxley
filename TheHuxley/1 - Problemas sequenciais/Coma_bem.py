#Faça um programa que leia um valor representando o gasto realizado por um cliente do restaurante COMABEM e imprima o valor total a ser pago, considerando os 10% do garçom.


valorgasto = float(input())

garcom = valorgasto * 10 / 100

print('{:.2f}'.format(valorgasto + garcom))
