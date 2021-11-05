psnr = float(input())
enq = str(input())
exp = str(input())

if(80 <= psnr <= 90):
    if(enq == "bom" or enq == "excelente"):
        if(exp == "bem exposta"):
            print("para imprimir")
        else:
            print("boa")
    else:
        print("marromeno")

elif(50 <= psnr < 80):
    if(enq == "excelente"):
        if(exp == "bem exposta"):
            print("boa")
    else:
        print("marromeno")

elif(psnr < 50):
    if(enq == "excelente"):
        if(exp == "bem exposta"):
            print("marromeno")
        else:
            print("lixo")
    else:
        print("lixo")
