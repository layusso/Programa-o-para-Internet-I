from  buscador import search
from buscador import print_text_Keyword
from buscador import create_table
from manipularTabelas import clean_table
from manipularTabelas import print_table
from manipularTabelas import table_to_array
import requests_cache

# Habilitar o cache
requests_cache.install_cache('meu_cache')

def main():
    cont = 0

    keyword = input("Digite a palavra chave: ")
    url = input("Digite a url: ")
    depth = int(input("Digite a profundidade: "))
    search(keyword, url, depth)

    while cont == 0:
        print(" 1 - Imprimir páginas rankeadas  2- Fechar programa: ")
        option1 = int(input("Digite o número da operação: "))

        if option1 == 1:
            print_table()
            array = table_to_array()
            option = int(input("Digite o número do link que deseja buscar os trechos com a keyword: "))
            print_text_Keyword(keyword, array[option][0])
            cont += 1
        else:
            cont+= 1


    clean_table()

main()
