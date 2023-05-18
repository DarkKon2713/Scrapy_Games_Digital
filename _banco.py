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
                conexao=sqlite3.connect("_jogos.db")
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

pesquisa_banco()
