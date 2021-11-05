'''Guido é um cientista, ele foi chamado para resolver um problema da usina do senhor Ambrósio. Senhor Ambrósio quer construir uma usina de tratamento de água onde o aproveitamento do espaço seja o melhor possível. Ele lhe deu uma folha que contém o raio dos locais onde pretende fazer os tanques redondos.
Ele espera receber de Guido dados que contenham a área de cada tanque o qual lhe deu o raio.
Porém Guido está muito atarefado e pediu sua ajuda para fazer um programa que possa calcular a área de cada tanque de forma mais rápida.
Considerando que para este problema π = 3.14159. 
- Efetue o cálculo da área.'''


raio = float(input())

area = (3.14159 * (raio**2))

print('Area = {:.4f}'.format(area / 10000))
