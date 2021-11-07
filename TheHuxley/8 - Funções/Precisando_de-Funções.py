'''Escreva um programa que receba como entrada 5 números inteiros positivos. 
Cada número lido da entrada vai gerar um novo valor que depende do seguinte:
Se o número lido da entrada for múltiplo de 3, o novo valor será o fatorial do número lido;
Se o número lido da entrada NÃO for múltiplo de 3, o novo valor será dado por S em que S é o resultado da série:
S = num/fat(0) + num/fat(1) + num/fat(2) + ... + num/fat(num)
Em que, fat(x) corresponde ao fatorial do número x.
O resultado deve ser a soma dos valores gerados a partir de cada número lido.
Para isso, é obrigatório a criação de três funções: uma para calcular o fatorial de um número, uma para calcular o valor de S e uma para verificar se um número é ou não múltiplo de 3'''


def fat(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
    
def serie(s):
    somato = 0
    for num in range(s+1):
        fra = s/fat(num)
        somato+=fra
    return somato

def mult(n):
    if n%3 == 0:
        return 'true'
    else:
        return 'false'
    
    
lista = []
for i in range(5):
    numeros = int(input())
    if mult(numeros) == 'true':
        lista.append(fat(numeros))
    else:
        lista.append(serie(numeros))
        
print('{:.2f}'.format(sum(lista)))
