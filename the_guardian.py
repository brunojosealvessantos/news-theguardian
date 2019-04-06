import requests
import json
import pandas as pd


def exportar_csv(titulo, link, nome):
    df=pd.DataFrame({'Titulo' : titulo, 'Link' : link,})
    df.to_csv("%s.csv" %nome, index = False, sep = ";", encoding = 'utf-8-sig')
    print("Arquivo esportado com sucesso para pasta do projeto!")

def busca_noticias(dados):
    titulo = []
    link = []
    for posicao in dados['response']['results']:
        print(posicao["webTitle"])
        print(posicao["webUrl"])
        print("------------------------------------------------------------------------------")
        titulo.append(posicao['webTitle'])
        link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post. Tente mais tarde!")
    else:
        exportar_csv(titulo, link, "noticias" )

def busca_sports(dados):
    titulo=[]
    link=[]
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'Sport':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post referente a esporte. Tente mais tarde")
    else:
        exportar_csv(titulo, link, "sports")
    
def busca_news(dados):
    titulo=[]
    link=[]
    for posicao in dados['response']['results']:
        if posicao['pillarName']=='News':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post referente a News. Tente mais tarde")
    else:
        exportar_csv(titulo, link, "News")

def busca_arts(dados):
    titulo=[]
    link=[]
    for posicao in dados['response']['results']:
        if posicao['pillarName']=='Arts':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post referente a Arts. Tente mais tarde")
    else:
        exportar_csv(titulo, link, "Arts")

def main():
    url = "https://content.guardianapis.com/search?api-key=c52ee909-5d2c-47b7-9554-6146ae49e22a"
    print("Acessando Base de Dados...")
    response = requests.get(url)
    if response.status_code==200:
        print("Acessando a base de dados do The guardian...")
        dados = response.json()
        try:
            escolha = int(input("Digite o numero da escolha que deseja baixar: \n\t1 - Sport;\n\t2 - News;\n\t3 - Art;\n\t4 - Buscar Noticias\n\t0 - Sair\n\n -->"))
        except:
            print("Por favor digite apenas números")
        if escolha > 4 or escolha < 0:
            print("Por favor digite números estre 0 e 4")
        elif escolha == 1:
            busca_sports(dados)
        elif escolha == 2:
            busca_news(dados)
        elif escolha == 3:
            busca_arts(dados)
        elif escolha == 4:
            busca_noticias(dados)
        elif escolha == 0:
            print("Obrigado por utilizar o programa.")
    else:
        print("Não foi possivel acessar a base de dados.")
if __name__ =="__main__":
    main()

