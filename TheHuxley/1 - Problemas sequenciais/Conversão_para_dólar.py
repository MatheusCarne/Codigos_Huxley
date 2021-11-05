#Escreva um programa que realize a conversão de dólar para real: para cada valor lido em dólar da entrada padrão, será exibido o correspondente em reais (1 dólar = 3.55 reais).


dolar = float(input())
conv = dolar * 3.55
print('%.2f' % conv)
