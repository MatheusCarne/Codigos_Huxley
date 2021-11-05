'''A Entidade ganhou N ímãs no seu aniversário, ela achou muito interessante a forma como eles se atraem e repulsam. Certo dia ela estava andando num corredor com sua caixa de ímãs, e só no final do corredor, percebeu que a caixa estava furada. Todos os ímãs caíram, um ímã depois do outro. Mas ela achou muito interessante, pois formaram-se K grupos de ímãs, além disso, ela percebeu que existia um grupo com X ímãs.

Ela quer fazer algumas análises probabilísticas, mas ela não quer perder tempo contando quantos grupos e qual o maior grupo existe. Então, ela quer que você faça um programa que faça essa contagem por ela.

Exemplo: 6 ímãs caíram na seguinte ordem:
10
10
10
01
10
10'''


imas = int(input())
polo1 = 0
grupos = 0
grupos1 = 0
grupo = 0
for i in range(imas):
    polo = int(input())
    
    if i == 0:
        
        polo1 = polo
        grupos +=1
        grupo +=1
    else:
        if polo == polo1:
            grupos +=1
            polo1 = polo
        else:
            polo1 = polo
            if grupos1 < grupos:
                grupos1 = grupos
            grupo +=1
            grupos = 1
            
if grupos1> grupos:
    print('groups: {}, biggest: {}'.format(grupo,grupos1))
else:
    print('groups: {}, biggest: {}'.format(grupo, grupos))
