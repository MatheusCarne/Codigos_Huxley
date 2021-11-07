let = ['@', '3', '1', '0', '7', '5']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pa = str(input())
nova = ""
cont = 0
qnt = 0
if(pa == " "):
    print("erro")
    print(0)
    
else:
    for i in range(len(pa)):
        if(pa[i] in num):
            print("numeros")
            print(0)
            cont = 1
            break
        elif(pa[i] == "a" or pa[i] =="A"):
            nova += "@"
            qnt +=1
        elif(pa[i] == "e" or pa[i] == "E"):
            nova += "3"
            qnt +=1
        elif(pa[i] == "i" or pa[i] == "I"):
            nova += "1"
            qnt +=1
        elif(pa[i] == "o" or pa[i] == "O"):
            nova += "0"
            qnt += 1
        elif(pa[i]== "t" or pa[i]== "T"):
            nova += "7"
            qnt += 1
        elif(pa[i] == "s" or pa[i]=="S"):
            nova+= "5"
            qnt += 1
        else:
            nova += pa[i]

    if(cont != 1):
        print(nova[::-1])
        print(qnt)
