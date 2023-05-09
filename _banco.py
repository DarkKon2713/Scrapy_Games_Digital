import sqlite3
import os
from datetime import date
os.system('cls' if os.name == 'nt' else 'clear')#limpar terminarl


lojas=['eshop','nuuvem','psn','steam']
rowlist_banco=[]
def pesquisa_banco():   
    pesquisa_line=input("Digite o nome do jogo: ")
    print('Filtrar Data ')
    data_pesquisa=input("Digite a data da pesquisa(XX/XX/XXXX): ")
    filtro="jogo"
    order_by='ASC'
    for loja_ in lojas:
            try:
                conexao=sqlite3.connect("jogos.db")
                cursor=conexao.cursor()
                if pesquisa_line!='':
                    cursor.execute(f"SELECT * FROM {loja_} WHERE jogo LIKE '%{pesquisa_line}%' order by  {filtro} {order_by};")
                if pesquisa_line=='':
                    cursor.execute(f"SELECT * FROM {loja_}  order by  {filtro} {order_by};")
                if pesquisa_line=='#x#':
                    cursor.execute(f"SELECT * FROM {loja_} ORDER BY LENGTH ({filtro}) {order_by};")
                resultado=cursor.fetchone()
                while True:
                    resultado=cursor.fetchone()
                    if resultado is None:
                        break
                    
                    loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data=resultado
                    
                    rowlist_banco.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data))
                cursor.close()
                conexao.close()
            except:
                    print('listra ainda nao criada')
    print_(data_pesquisa)
def print_(data_pesquisa):
    for r in rowlist_banco:
        loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data=r
        if data_pesquisa=='':
            print(loja.upper(),jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data)   
        if data_pesquisa==data:
            print(loja.upper(),jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data)
    print('')
print(len('https://loja.karcher.com.br/_v/segment/graphql/v1?workspace=master&maxAge=short&appsEtag=remove&domain=store&locale=pt-BR&operationName=productSearchV3&variables=%7B%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2240e207fe75d9dce4dfb3154442da4615f2b097b53887a0ae5449eb92d42e84db%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6ZmFsc2UsInNrdXNGaWx0ZXIiOiJBTEwiLCJwcm9kdWN0T3JpZ2luVnRleCI6ZmFsc2UsIm1hcCI6ImMiLCJxdWVyeSI6ImxhdmFkb3Jhcy1kZS1hbHRhLXByZXNzYW8iLCJmcm9tIjoxMiwidG8iOjIzLCJzZWxlY3RlZEZhY2V0cyI6W3sia2V5IjoiYyIsInZhbHVlIjoibGF2YWRvcmFzLWRlLWFsdGEtcHJlc3NhbyJ9XX0%3D%3D%22%7D'))
