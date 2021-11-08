'''Escreva um programa que recebe informações de várias figuras geométricas  e, em seguida, imprime um resumo das características (área e comprimento) dessas figuras. 
O programa pode receber até 3 tipos de figuras: quadrado, retângulo e círculo, identificados pela primeira letra da figura. 
Caso as dimensões da figura forem negativas, o resultado do cálculo das características será -1. O programa encerrará quando o usuário digitar sair no tipo da figura.
Use funções para modularizar seu programa. 
Faça uma função para cada cálculo de característica de uma figura. Faça também uma função para imprimir o resumo final.
Obs.: Use pi = 3.14 e o resultado com 2 casas decimais de aproximação.'''


def circulo(raio):
    return 3.14*raio*raio

def rentagulo(base,altura):
    return base*altura

def quadrado(lado):
    return lado*lado

cont_figuras = cont_circulo = 0
maior_c = maior_q = maior_r = 0

figuras = input().lower()

while figuras != "sair":
    cont_figuras +=1
    if figuras == "c":
        cont_circulo += 1
        numeros = int(input())
        if numeros == -1:
            tamanho = -1
            maior_c = tamanho
        else:
            tamanho = circulo(numeros)
        if tamanho > maior_c:
            maior_c = tamanho
    elif figuras == "r":
        base = int(input())
        altura = int(input())
        if base == altura == -1:
            tamanho = -1
            maior_r = tamanho
        else:
            tamanho = rentagulo(base,altura)
        if tamanho > maior_r:
            maior_r = tamanho
    elif figuras == "q":
        numeros = int(input())
        if numeros == -1:
            tamanho = -1
            maior_q = tamanho
        else:
            tamanho = quadrado(numeros)
        if tamanho > maior_q:
            maior_q = tamanho
    figuras = input().lower()


print("Maior circulo: %.2f"%(maior_c))
print("Maior retangulo: %.2f"%(maior_r))
print("Maior quadrado: %.2f"%(maior_q))
print("Quantidade de figuras %.0f"%(cont_figuras))
print("Percentual de circulos: %.2f"%((cont_circulo/cont_figuras)*100))
