import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.skysports.com/premier-league-table"

    conteudo = requests.get(url)


    if conteudo.status_code == 200:
        soup = BeautifulSoup(conteudo.content, "html.parser")
        tabela = soup.find("table", {"class": "standing-table__table"})

        for row in tabela.find_all("tr"):
            celulas = row.find_all("td")
            if len(celulas) > 0:
                print(celulas[0].text.strip(), celulas[1].text.strip(), celulas[2].text.strip())
    else:
        print("Erro ao fazer a requisição")

main()