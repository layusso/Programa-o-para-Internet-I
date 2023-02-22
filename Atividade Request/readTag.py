import requests
from bs4 import BeautifulSoup

def main():
    pagina = requests.get("https://pt.wikipedia.org/wiki/Wikipédia:Página_principal")


    if pagina.status_code == 200:
        conteudo = pagina.content
        soup = BeautifulSoup(conteudo, "html.parser")

        tag = input("Digite a tag que deseja pesquisar: ")
        tag_conteudo = soup.find(tag).prettify()
        print(tag_conteudo)


    else:
        print("A solicitação falhou!")

main()