naci = input().lower()
ocu= input().lower()
quant= int(input())
cali= int(input())

if naci == ('e'):
  if quant ==0:
    print('Liberado')
  else:
    print('Barrado')
elif naci == ('b'):
  if ocu == ('m'):
    print('Liberado')
  elif ocu == ('t') or ocu ==('o'):
    print('Liberado' if quant <=1 and cali<=22 else 'Barrado')
  elif ocu ==('c'):
    print('Liberado' if quant <=2 and cali<=38 else 'Barrado')
