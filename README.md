<h1 align="center">Análise das Músicas Mais <br> Populares ao Longo do Tempo 🎵</h1>
<br>

## Integrantes
* [Irlan Miguel de Oliveira Honorato](https://github.com/irlan06)
* [José Victor Justino de Oliveira](https://github.com/victorjtn)
* [Labert Paixão Ribeiro](https://github.com/laberttt)

## Abordagem de Coleta dos Dados
- Utilização de APIs como Spotify, YouTube, Genius para obter informações das músicas.
- Os dados coletados incluirão: nome da música, artista, ano de lançamento, número de streams/vendas, posição nos rankings e gênero musical.
- O dataset será atualizado mensalmente ou semestralmente, dependendo da disponibilidade dos dados.

## Drescrição do conjunto de dados 📌
Este projeto coleta e armazena as 100 músicas mais populares de cada ano dentro de um intervalo especificado, utilizando a API do Spotify. Os dados incluem informações como nome da música, artista, álbum, duração, gênero, ID da faixa, data de lançamento e popularidade.

## Processo de Coleta dos dados 🔍
Os dados são coletados por meio da API do Spotify, utilizando a biblioteca spotipy em Python. O script realiza buscas por ano, com isso, filtrando as músicas mais populares e organizando os resultados de forma decrescente por popularidade. A coleta é feita usando credenciais da API, armazenadas de forma segura em variáveis de ambiente.

## Estrutura dos Dados 📊
Cada linha do conjunto de dados representa uma música, e as colunas são as seguintes:

| Nome da Coluna   | Descrição | Exemplo |
|-----------------|------------|---------|
| Year           | Ano da música | 2023 |
| Track          | Nome da música | "Blinding Lights" |
| Artist        | Nome do(s) artista(s) | "The Weeknd" |
| Album         | Nome do álbum | "After Hours" |
| Duration (s)  | Duração da faixa em segundos | 200 |
| Genres        | Gênero musical | "Pop, R&B" |
| Track ID      | ID único da música no Spotify | "0VjIjW4GlUZAMYd2vXMi3b" |
| Release Date  | Data de lançamento | "2019-11-29" |
| Popularity    | Popularidade (0 a 100) | 95 |

## Acesso aos dados 📂
Os dados coletados estão armazenados em um arquivo CSV e podem ser acessados por meio do seguinte link do Google Drive:
[**Music Data Analytics**](https://drive.google.com/file/d/1ht1N0jPmwRCvgLsZfkbd9uGZaLAoqtGT/view?usp=sharing)