import requests

def main():
    cep = input("Digite o CEP a ser pesquisado: ")
    url = "https://viacep.com.br/ws/{}/json/".format(cep)


    conteudo = requests.get(url)

    if conteudo.status_code == 200:
        data = conteudo.json()

        if "erro" not in data:
            endereco = data["logradouro"] + ", " + data["bairro"] + ", " + data["localidade"] + " - " + data["uf"]
            print("Endereço: " + endereco)
        else:
            print("CEP não encontrado.")
    else:
        print("Falha na solicitação da API.")

main()