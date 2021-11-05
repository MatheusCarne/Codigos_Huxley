'''Os funcionários de uma empresa chamada QUALQUER S.A vão se confraternizar e como sempre acontece, começou a se discutir qual seria o valor mais justo a ser pago por cada um. O problema é que há pessoas que ganham mais e são beneficiadas em outras situações. 
Então eles fizeram o seguinte para estimular cada um a dar o máximo que pudesse: cada um daria um valor igual ou inferior ao total sem ver quanto os demais dariam. Ao final se calcularia a média e quem deu o maior valor de todos receberia o excedente.
Para isso nosso programa vai receber um valor N (número de funcionários), o valor total da conta, o nome e o valor pago de cada um dos N funcionários e ao final vai exibir o valor da conta, a média, o nome de quem pagou mais e o excedente.'''


valortotal = float(input())
quant = int(input())
maiorvalor = 0
pagoumais = ''
somavalor = 0

for i in range(quant):
   nome = str(input())
   valor = float(input())
   somavalor+=valor
   if i == 0:
        maiorvalor = valor
        pagoumais = nome
   else:
        if valor > maiorvalor:
            maiorvalor = valor 
            pagoumais = nome
print('{} pagou R$ {}'.format(pagoumais, maiorvalor))
if somavalor > valortotal:
    print('Valor excedente: sobra R$ {}'.format(somavalor - valortotal))
else:
    print('Valor insuficiente: falta R$ {}'.format(valortotal - somavalor))
