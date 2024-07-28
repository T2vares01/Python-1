import requests
from bs4 import BeautifulSoup as bs

def pesquisa():
    link = "https://www.google.com/search?q=cotacao+dolar"
    headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    requisicao = requests.get(link, headers = headers)
    rt = requisicao.text # codigo da pagina
    site = bs(requisicao.text ,"html.parser") # organizar o codigo do site

    pesquisa = site.find("textarea",class_ = "gLFyf")
    dolar = site.find("span" ,class_="SwHCTb")

    # print(request) # verificação se der certo vai dar 200
    # print(site.prettify()) # o site em html

    print("O dolar esta como o valor de R$:{}".format(dolar["data-value"]))

if __name__ == "__main__":
    pesquisa()