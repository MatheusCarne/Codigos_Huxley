'''Um empresário está querendo abrir um novo lugar de entretenimento na cidade e contratou você para criar um sistema de venda ingressos. Ele ainda não sabe no que vai investir, pode ser um cinema, um ginásio esportivo, um teatro...
Ele te informa que os ingressos terão um valor de R$ 15,00 de segunda-feira a quinta-feira, e de sexta-feira a domingo o valor do ingresso será dobrado.
- Em qualquer dia da semana, estudantes tem desconto de 30% no ingresso.
- Nos finais de semana, sócios tem desconto de 20% no ingresso.
Obs: Não existe a possibilidade de um cliente ser sócio e estudante!'''


diasemana = int(input())
estudante = int(input())
socio = int(input())

if diasemana == 1 or diasemana == 2 or diasemana == 3 or diasemana == 4 :
    if estudante == 1:
        print('ESTUDANTE: R$ {:.2f}'.format(15-(15*30/100)))
    elif socio == 1:
        print('SOCIO: R$ {:.2f}'.format(15))
    else:
        print('COMUM: R$ {:.2f}'.format(15))
elif diasemana == 5 or diasemana == 6 or diasemana == 7:
    if estudante == 1:
        print('ESTUDANTE: R$ {:.2f}'.format(30-(30*30/100)))
    elif socio == 1:
        print('SOCIO: R$ {:.2f}'.format(30-(30*20/100)))
    else:
        print('COMUM: R$ {:.2f}'.format(30))
