def cadastrar_jogador(nome, partidas):

    media = sum(partidas) / len(partidas)

    jogador = {
        "nome": nome,
        "gols": partidas,
        "total": sum(partidas),
        "media": media
    }

    print(jogador)


cadastrar_jogador("João", [1, 0, 3, 2])