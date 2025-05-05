import os
import json
import csv

if not os.path.exists("dados"):
    os.makedirs("dados")

arquivo_json = "dados/dados.json"
def salvar_json (dados, arquivo_json):
    with open(arquivo_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

arquivo_csv = "dados/dados.csv"
def salvar_csv(dados, arquivo_csv):
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=  ["ID","nome", "email", "telefone"])
        writer.writeheader()
        writer.writerows(dados)


from faker import Faker

fake = Faker()
def gerar_dados(qtd):
    dados = []
    for i in range(1, qtd + 1):
        pessoa = {
            "ID": i,
            "nome": fake.name(),
            "email": fake.email(),
            "telefone": fake.phone_number()
        }
        dados.append(pessoa)
    return dados

dados_gerados = gerar_dados(5)

for pessoa in dados_gerados:
    print(pessoa)

if __name__ == "__main__":
    dados_gerados = gerar_dados(10)
    salvar_json(dados_gerados, "dados/dados.json")
    salvar_csv(dados_gerados, "dados/dados.csv")
    print("Dados gerados com sucesso!")
