#Faça um programa que calcule e mostre a área de um trapézio


basemaior = int(input())
basemenor = int(input())
altura = int(input())
area = ((basemaior + basemenor) * altura) / 2
print('{:.1f}'.format(area))
