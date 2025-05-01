import requests
from bs4 import BeautifulSoup
import csv
import time

ano = 2009
rankings = []

while ano <= 2023:
    
    KWORB_URL = f"https://kworb.net/youtube/topvideos{str(ano)}.html"

    # Fazendo a requisição HTTP
    response = requests.get(KWORB_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrando a tabela de rankings
    tabela = soup.find("table", class_="addpos sortable")

    # Criando uma lista para armazenar os dados
    position = 1
    # Iterando pelas linhas da tabela (ignorando o cabeçalho)

    for linha in tabela.find_all("tr")[1:101]:
        colunas = linha.find_all("td")
        
        nome = colunas[0].text.strip()
        streams = colunas[1].text.strip()
        
        rankings.append([ano, position, nome, streams])
        position += 1

    ano += 1

    time.sleep(60)
    

# Salvando os dados em um CSV
with open("kworb_youtube_top100_PerYear.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Ano", "Posição", "Música", "Streams"])
    writer.writerows(rankings)

print("Arquivo CSV gerado com sucesso!")
