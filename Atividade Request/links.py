import requests
from bs4 import BeautifulSoup


def main():
    pagina = requests.get("https://pt.wikipedia.org/wiki/Wikipédia:Página_principal")

    if pagina.status_code == 200:
        conteudo = pagina.content
        soup = BeautifulSoup(conteudo, "html.parser")
        links = soup.find_all("a")

        for i in links:
            print(i.get("href"))

    else:
        print("A solicitação falhou!")


main()