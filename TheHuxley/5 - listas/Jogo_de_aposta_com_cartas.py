while True:
  nomes = []
  conversao_int = [] 
  jogo = str(input()).split()
  if jogo == ['sair']:
    print('fim')
    break
  nomes.extend([jogo[0], jogo[1]])
  jogo.pop(0)
  jogo.pop(0)
  if len(jogo) % 2 != 0:
    print('erro')
    break
  else:
    for nums in jogo:
      conversao_int.append(int(nums))
    contador = 0
    jogador1 = 0
    jogador2 = 0
    for nums in range(len(conversao_int)):
      if (nums + 1) % 2 != 0:
        contador += 1
        if conversao_int[nums] == conversao_int[nums + 1]:
          if contador % 2 != 0:
            jogador1 += (conversao_int[nums] + conversao_int[nums]) * 2
          else:
            jogador2
        elif (conversao_int[nums] + 1 == conversao_int[nums + 1]) or (conversao_int[nums] == conversao_int[nums + 1] + 1):
          if contador % 2 != 0:
            jogador1 += (conversao_int[nums] + conversao_int[nums + 1]) * 3
          else:
            jogador2 += (conversao_int[nums] + conversao_int[nums + 1]) * 3
        else:
          if contador % 2 != 0:
            jogador1 += (conversao_int[nums] + conversao_int[nums + 1])
          else:
            jogador2 += (conversao_int[nums] + conversao_int[nums + 1])
    if jogador1 > jogador2:
      print(nomes[0])
    elif jogador1 < jogador2:
      print(nomes[1])
    else:
      print('empate')
