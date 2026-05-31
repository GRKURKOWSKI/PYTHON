import requests

API_KEY = "4d034d5a6b90064571dd976a5c6499b5"

cidades_monitoradas = ["São Paulo", "London", "Tokyo", "New York", "Paris"]


class CidadeClima:

    def __init__(self, nome, temperatura, umidade, condicao):
        self.nome = nome
        self.temperatura = temperatura
        self.umidade = umidade
        self.condicao = condicao

    def __str__(self):
        linha = "-" * 40
        return (
            f"{linha}\n"
            f"  {self.nome}\n"
            f"{linha}\n"
            f"  Temp    : {self.temperatura:.1f}°C\n"
            f"  Umidade : {self.umidade}%\n"
            f"  Tempo   : {self.condicao}\n"
        )


def obter_dados_cidade(nome_cidade):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    try:
        r = requests.get(endpoint, params={
            "q": nome_cidade,
            "appid": API_KEY,
            "units": "metric",
            "lang": "pt_br"
        }, timeout=10)

        if r.status_code == 404:
            print(f"Cidade nao encontrada: {nome_cidade}")
            return None

        if r.status_code == 401:
            print("Chave de API invalida ou nao ativada.")
            return None

        r.raise_for_status()
        j = r.json()

        return CidadeClima(
            nome=j["name"],
            temperatura=j["main"]["temp"],
            umidade=j["main"]["humidity"],
            condicao=j["weather"][0]["description"].capitalize()
        )

    except requests.exceptions.ConnectionError:
        print(f"Erro de conexao ao buscar {nome_cidade}.")
    except requests.exceptions.Timeout:
        print(f"Timeout ao buscar {nome_cidade}.")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP em {nome_cidade}: {e}")
    except KeyError:
        print(f"Resposta inesperada da API para {nome_cidade}.")

    return None


relatorio_clima = []

print("\nBuscando dados climaticos...\n")

for cidade in cidades_monitoradas:
    dados = obter_dados_cidade(cidade)
    if dados:
        relatorio_clima.append(dados)

print("\n========================================")
print("       RELATORIO CLIMATICO FINAL")
print("========================================\n")

for item in relatorio_clima:
    print(item)

print(f"Cidades obtidas com sucesso: {len(relatorio_clima)} de {len(cidades_monitoradas)}")