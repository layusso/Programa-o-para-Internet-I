import requests

def main():
    endereco = input("Digite o endereço de imagem")

    url = endereco
    nome_arquivo = "imagem_local.jpg"

    conteudo = requests.get(url)

    with open(nome_arquivo, 'wb') as arquivo_local:
        arquivo_local.write(conteudo.content)

main()