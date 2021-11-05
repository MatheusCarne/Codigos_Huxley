#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


num = int(input())

if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda')
elif num == 3:
    print('Terca')
elif num == 4:
    print('Quarta')
elif num == 5: 
    print('Quinta')
elif num == 6:
    print('Sexta')
elif num == 7:
    print('Sabado')
elif num > 7:
    print('valor invalido')
