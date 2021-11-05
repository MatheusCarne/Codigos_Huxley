'''Eu sou fanático pela letra a. 
Para mim, é muito importante saber quantas vezes a letra a aparece em qualquer texto. 
Você pode me ajudar? Crie um programa que leia um texto qualquer e me diga quantas vezes a letra a aparece nele.

OBS: desconsidere acentos, como ã e à.'''


frase = str(input()).lower()
print(frase.count('a'))
