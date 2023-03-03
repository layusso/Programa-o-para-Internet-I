from  buscador import search, print_text_Keyword
from manipularTabelas import clean_table, print_table, table_to_array

'''Url de testes :

https://solnic.codes/   key(ruby)
https://sandimetz.com/blog

'''

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
