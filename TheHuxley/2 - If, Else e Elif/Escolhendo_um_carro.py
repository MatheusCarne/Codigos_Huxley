'''Faça um programa que verifique as condições de um carro e dê uma indicação à Henrique para a compra ou não do carro.

Para ser considerado o carro deve atender a todos os requisitos obrigatórios. Feito isso, você deve verificar os requisitos desejáveis antes de imprimir uma mensagem.
Se não atender os requisitos obrigatórios, imprima a mensagem "Não compre!"
Caso ele atenda a todos os requisitos desejáveis, imprima na saída a mensagem "Pode comprar!"
Caso ele atenda a apenas 2 requisitos desejáveis, imprima a mensagem "Boa compra."
Caso ele atenda a apenas 1 requisito desejável, imprima a mensagem "Pode ser uma opção."
Caso o carro não atenda nenhum requisito desejável, imprima a mensagem "Recomendo pensar melhor..."'''


esp = str(input()).upper()
port = str(input()).upper()
valor = float(input())
motor = float(input())
camb = str(input()).upper()

if esp == 'C' or port == 'P':
  print('Não compre!')
elif valor < 100000 and motor >= 1.5 and camb == 'A':
  print('Pode comprar!')
elif valor < 100000 and motor >= 1.5 or motor >= 1.5 and camb == 'A' or valor < 100000 and camb == 'A':
  print('Boa compra.')
elif valor < 100000 or motor >= 1.5 or camb == 'A':
  print('Pode ser uma opção.')
else:
  print('Recomendo pensar melhor...')
