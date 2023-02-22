import requests

def main():
    url = "https://www.google.com/search"

    pesquisa = input("Digite o termo de pesquisa: ")

    params = {"q": pesquisa}

    conteudo = requests.get(url, params=params)

    if conteudo.status_code == 200:
        print(conteudo.content)
    else:
        print("A requisição falhou!")

main()