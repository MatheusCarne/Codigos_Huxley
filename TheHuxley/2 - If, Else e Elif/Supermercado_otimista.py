'''José está prestes a inaugurar seu supermercado. Ele acredita que o cidadão brasileiro é capaz de pagar suas compras sozinho, sem precisar de um funcionário para conferir se o que ele está pagando corresponde aos produtos que ele está levando. 
Para isso ele vai precisar de um programa que irá ler o dia da semana, o preço do produto, a opção do produto ("prata" ou "ouro") e o nome. 
Se a compra estiver sendo realizada na segunda, terça ou quarta e a opção do produto for "ouro", o preço do produto ficará pela metade. 
Se a compra estiver sendo realizada na quinta ou sexta e o preço estiver entre R$ 10.00 e R$ 100.00, o preço será reduzido para um terço do valor original.
Se a compra estiver sendo realizada no sábado e a opção for prata, o preço do produto será o triplo.
Em qualquer outro caso, o preço será o dobro.'''


dia = str(input())
preco = float(input())
op = str(input())
nome = str(input())
precon = float(0)

if(dia == "seg" or dia == "ter" or dia == "qua"):
    if(op == "ouro"):
        precon = preco/2
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
    else:
        precon = 2*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)

elif(dia == "qui" or dia == "sex"):
    if(10 <= preco <= 100):
        precon = preco/3
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
    else:
        precon = 2*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)

elif(dia == "sab"):
    if(op == "prata"):
        precon = 3*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
    else:
        precon = 2*preco
        print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)

else:
    precon = 2*preco
    print("O preco do produto", nome,"no dia",dia,"eh", "%.2f" % precon)
