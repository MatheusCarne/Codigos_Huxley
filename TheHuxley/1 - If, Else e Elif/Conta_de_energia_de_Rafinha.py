'''Rafinha sabe que em sua cidade o valor da KWh de energia varia da forma mostrada abaixo.

Até 99 KWh: R$1.35
100 até 299 KWh: R$1.55
300 até 574 KWh: R$1.75
Maior ou igual a 575 KWh: R$2.15
Ele também sabe que quando o consumo é maior que 300KWh é cobrado uma taxa de 10% no valor da conta e o preço mínimo de qualquer conta é R$35. Escreva um programa para auxiliar Rafinha a visualizar o valor de sua conta elétrica e qual o valor do KWh aplicado em sua conta.
OBS: O formato da saída deve ser feito com duas casas decimais.'''

energia = int(input())

if energia >= 26 and energia <= 99:
    print('{:.2f}\n{}'.format(energia*1.35,1.35))
elif energia <= 25:
  print('35.00\n1.35')
elif energia >= 100 and energia <=299:
  print('{:.2f}\n{}'.format(energia*1.55,1.55))
elif energia >= 300 and energia <=574:
  print('{:.2f}\n{}'.format((energia*1.75)*1.1,1.75))
elif energia >= 575:
  print('{:.2f}\n{}'.format((energia*2.15)*1.1,2.15))
