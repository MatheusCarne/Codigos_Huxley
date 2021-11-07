lista1 = []
lista2 = []
soma = sub = 0

dimen = int(input())

for i in range(dimen):
    for j in range(1):
        entradas1 = input().split()
        lista1.append(entradas1)


for i in range(dimen):
    for j in range(1):
        entradas2 = input().split()
        lista2.append(entradas2)

sinais = input()

if sinais == '+-':
    for i in range(dimen):
        for j in range(dimen):
            if i % 2 == 0:
                soma = float(lista1[i][j]) + float(lista2[i][j])
            else:
                soma = float(lista1[i][j]) - float(lista2[i][j])
            if j + 1 == dimen:
                print('{:.2f}'.format(soma))
            else:
                print('{:.2f}'.format(soma), end=' ')

elif sinais == '-+':
    for i in range(dimen):
        for j in range(dimen):
            if i % 2 == 1:
                sub = float(lista1[i][j]) + float(lista2[i][j])
            else:
                sub = float(lista1[i][j]) - float(lista2[i][j])
            if j + 1 == dimen:
                print('{:.2f}'.format(sub))
            else:
                print('{:.2f}'.format(sub), end=' ')
