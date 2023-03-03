from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import sqlite3
import requests_cache
import re

PAGES_DB="pages.sqlite"
# Habilitar o cache
requests_cache.install_cache('meu_cache')


def increment_cont_if_exists(url):
    conn = sqlite3.connect(PAGES_DB)
    cursor = conn.cursor()

    # Verifica se a url já existe na tabela
    cursor.execute("SELECT cont FROM contPages WHERE url = ?", (url,))
    row = cursor.fetchone()
    if row is None:
        # Adiciona a url na tabela com cont = 1
        cursor.execute("INSERT INTO contPages (url, cont) VALUES (?, 1)", (url,))
    else:
        # Incrementa o cont para essa url
        cont = row[0] + 1
        cursor.execute("UPDATE contPages SET cont = ? WHERE url = ?", (cont, url))

    conn.commit()
    conn.close()



def search_content_in_database(url):
    conn = sqlite3.connect(PAGES_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            url TEXT PRIMARY KEY,
            content TEXT
        )
    """)

    cursor.execute("SELECT content FROM pages WHERE url = ?", (url,))# busca o contúdo da página ou None
    return cursor.fetchone()# retorna o conteúdo buscado

def insert_in_Page(url, content):
    conn = sqlite3.connect(PAGES_DB)#conecta-se com o bd
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pages (url, content) VALUES (?, ?)", (url, content))
    conn.commit()#adiciona / salva no bd


def print_text_Keyword(keyword, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contents = soup.find_all(string=re.compile(keyword))

    for content in contents: #percorre todas as tags da página
           
            '''text = tag.text.strip() # remove espaços em branco adicionais
            index = text.find(keyword)#posição da palavra-chave dentro do texto 
            start = max(0, index - 20)
            end = min(len(text), index + len(keyword) + 20)
            snippet = text[start:end]'''
            print(content.get_text()) 
            
      

def search(keyword, url, depth):
    result = search_content_in_database(url)
    print(url)
    if result is not None:
        # página já baixada, recupera o conteúdo do banco de dados
        content = result[0]
    else:
         # página ainda não foi baixada, faz a requisição GET e salva no banco de dados
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content = response.content
                insert_in_Page(url, content)
                

            else:
                print(f"Erro ao acessar página: {response.status_code}")
                return
        except requests.exceptions.MissingSchema:
            return
        except requests.exceptions.InvalidSchema:
            return
        except requests.exceptions.ConnectionError:
            return
        
    increment_cont_if_exists(url)    
    soup = BeautifulSoup(content, "html.parser")

    if depth > 0:
        # busca recursivamente nos links da página atual
        for link in set(soup.find_all("a")):
            href = link.get("href")
            href = re.sub(r"#.+", "", href)
            if href is not None:
                new_url = urljoin(url, href) # função urljoin do módulo urllib.parse para resolver links relativos e transformá-los em links absolutos, usando a URL da página atual como base. 
                search(keyword, new_url, depth - 1)
            


