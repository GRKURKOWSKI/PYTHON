def ler_arquivo_partida(caminho_arquivo):
    jogadores = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(';')
                if len(partes) == 5:
                    nome, classe, kills, deaths, dano = partes
                    jogador = {
                        "nome": nome,
                        "classe": classe,
                        "kills": int(kills),
                        "deaths": int(deaths),
                        "dano": int(dano)
                    }
                    jogadores.append(jogador)
    return jogadores

def calcular_kda(kills, deaths):
    if deaths == 0:
        return kills
    else:
        return kills / deaths

def filtrar_por_classe(jogadores, classe):
    filtrados = []
    for jogador in jogadores:
        if jogador["classe"] == classe:
            filtrados.append(jogador)
    return filtrados

def main():
    caminho_arquivo = 'partida.txt'

    jogadores = ler_arquivo_partida(caminho_arquivo)

    maior_dano = max(jogadores, key=lambda j: j["dano"])
    print(f"Jogador com maior dano: {maior_dano['nome']} - {maior_dano['dano']} de dano")

    total_kills = 0
    for jogador in jogadores:
        total_kills += jogador["kills"]
    media_kills = total_kills / len(jogadores)
    print(f"Média de kills geral: {media_kills:.2f}")

    jogadores_kda_alto = []
    for jogador in jogadores:
        kda = calcular_kda(jogador["kills"], jogador["deaths"])
        if kda > 2.0:
            jogadores_kda_alto.append(jogador["nome"].upper())

    if jogadores_kda_alto:
        print("Jogadores com KDA maior que 2.0:")
        for nome in jogadores_kda_alto:
            print(f"- {nome}")
    else:
        print("Nenhum jogador com KDA maior que 2.0")

    classes_unicas = set()
    for jogador in jogadores:
        classes_unicas.add(jogador["classe"])

    print("\nJogadores por classe:")
    for classe in sorted(classes_unicas):
        jogadores_classe = filtrar_por_classe(jogadores, classe)
        print(f"\nClasse: {classe} ({len(jogadores_classe)} jogadores)")
        for jogador in jogadores_classe:
            print(f"- {jogador['nome']}")

if __name__ == "__main__":
    main()