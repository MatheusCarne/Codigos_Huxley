'''Escreva umprograma que leia uma matriz 3 x 3 de inteiros da entrada padrão e calcule a média de todos seus valores positivos, o menor  valor lido, o valor delta e a soma de todos os elementos que não estão na diagonal principal.

O delta é igual a 1 se o menor valor for par e 0 se for ímpar.'''


matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap = soma = media = delta = diago = cont = 0
menval = 1
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())
        soma+=matriz[i][j]
        if matriz[i][j] < menval:
            menval = matriz[i][j]
        if matriz[i][j] > 0:
            somap+=matriz[i][j]
            cont+=1
        if menval % 2 == 0:
            delta = 1
        if i == j:
            diago+=matriz[i][j]
print('{:.2f} {} {} {}'.format(somap/cont,menval,delta,soma-diago))
