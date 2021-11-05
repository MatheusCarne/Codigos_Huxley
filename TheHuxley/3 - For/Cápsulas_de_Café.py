'''Alguns professores do DCX adoram tomar café e decidiram adquirir uma cafeteira especial para a sala do Departamento. A cafeteira utiliza cápsulas de café de vários sabores para preparar a bebida, e cada cápsula prepara o equivalente a duas xícaras.
As cápsulas são vendidas em caixas pequenas (10 unidades) ou grandes (16 unidades), e ficou acertado que cada professor faria a doação de quantas caixas quisesse para o grupo.
Escreva um programa que receba como entrada a quantidade e o tamanho das caixas doadas por cada um dos sete professores que compartilham a cafeteira, e exiba a quantidade total de cápsulas de café doadas, e quantas xícaras cada professor poderá beber.'''


contP = 0
contG = 0

for cont in range(7):
    quan = int(input())
    taman = str(input()).lower()
    if taman == 'p':
        contP+=quan
    else:  
        contG+=quan
cap = ((contP*10)+(contG*16))
print('{}'.format(cap))
print('{:.0f}'.format((cap*2)/7))
