'''Faça uma função que escolhe o ataque titular da seleção brasileira baseado nas características de cada jogador. 
Cada característica será usada para compor um índice técnico que será usado para definir os titulares.'''


def nivel():
    maior = []
    for i in range(5):
        fora = 0
        nome = str(input())
        desem = int(input())
        if(desem == 0):
            fora += 1
        gols = int(input())
        if(gols == 0):
            fora+= 1
        cansaco = int(input())
        if(cansaco == 0):
            fora += 1
        entro = int(input())
        if(entro == 0):
            fora += 1

        if(fora >=2):
            indi = 0
        else:
            indi = desem*2+gols*3.5+cansaco*1.5+entro*2

        maior.append(indi)

    maior.sort()
    return maior

nivel = nivel()
print(nivel[-1])
print(nivel[-2])
print(nivel[-3])
