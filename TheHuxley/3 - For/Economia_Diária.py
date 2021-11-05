'''Poliana resolveu economizar dinheiro para comprar um carro.
Ela traçou como meta depositar um valor X em seu cofrinho no primeiro dia da semana, e ir guardando a cada manhã o valor do dia anterior acrescido de pelo menos R$ 0,50. Mas será que ela vai conseguir fazer isso todos os dias?
Para saber se o plano de Poliana vai dar certo, escreva um programa que receba como entrada o valor inicial depositado, e em seguida os valores depositados a cada dia. 
Ao final, exiba o total poupado e quantas vezes Poliana conseguiu cumprir sua meta.

Dica: é preciso sempre comparar o valor do dia com o do dia anterior'''


anterior = 0
soma = 0
lista = []
for i in [0,1,2,3,4,5,6]:
    dinh = float(input())
    soma+=dinh
    if dinh >= anterior +0.5:
        lista = lista + [dinh]
        anterior = dinh
    else:
        anterior = dinh
print('R$ {:.2f}\n{}'.format(soma,len(lista)-1))
