from dominio import Usuario, Lance, Leilao, Avaliador


huara = Usuario ("Huaraen")
rafael = Usuario ("Rafael")

lance_do_huara = Lance (huara, 100)
lance_do_rafa = Lance (rafael, 150)

leilao = Leilao("celular")

leilao.propoe(lance_do_huara)
leilao.propoe(lance_do_rafa)

for lance in leilao.lances:
    print ("O usuario {} deu um lance de {}".format (lance.usuario.nome, lance.valor))

avaliador = Avaliador()
avaliador.avalia(leilao)

print ("O menor lance foi de {} e o maior lance foi de {}". format (avaliador.menor_lance, avaliador.maior_lance))






