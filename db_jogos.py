
import sqlite3
lojas=['eshop','nuuvem','psn','steam']
rowlist_banco=[]
def pesquisa_banco(pesquisa_line,loja_pesquisa,filtro):
    order_by='ASC'
    if filtro=="Nome":
        filtro='jogo'
    if filtro=="Promoçao":
        filtro="tipo"
    if filtro=='Desconto':
        filtro='pdesconto'
        order_by='DESC'
    if filtro=='Preço':
        filtro='preco'
    if filtro=="Tipo":
        filtro='tipo'
    if filtro=="Data":
        filtro='data'
    

    if pesquisa_line =="limpar duply":
        
        for i in range(0, len(lojas)):
            conexao=sqlite3.connect("jogos.db")
            cursor=conexao.cursor()
            delete_query = f'''
DELETE FROM {lojas[i]}
WHERE rowid NOT IN (
SELECT MIN(rowid)
FROM {lojas[i]}
GROUP BY loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data
            
);
'''
            cursor.execute(delete_query)
            conexao.commit()
            conexao.close()
            print('feito')
    if loja_pesquisa =="Todos" and pesquisa_line!= "limpar duply":
        for loja_ in lojas:
            if pesquisa_line=="":
                try:

                    conexao=sqlite3.connect("jogos.db")
                    cursor=conexao.cursor()
                    if filtro!='preco':
                        cursor.execute(f"select * from {loja_} order by  {filtro} {order_by}")
                    if filtro=='preco':
                        cursor.execute(f"select * from {loja_} ORDER BY LENGTH({filtro}),{filtro}")
                    resultado=cursor.fetchone()
                    while True:
                        resultado=cursor.fetchone()
                        if resultado is None:
                            break
                        loja=resultado[0]
                        jogo=resultado[1]
                        preco=resultado[2]
                        pdesconto=resultado[3]
                        poriginal=resultado[4] 
                        linkcompleto=resultado[5] 
                        tipo=resultado[6]
                        data=resultado[7]
                        rowlist_banco.append((loja,data,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                        #print(loja,data,jogo,preco,pdesconto,poriginal,linkcompleto)
                
                    cursor.close()
                    conexao.close()
                except:
                    print('listra ainda nao criada')
            if pesquisa_line!="":
                try:
                    
                    conexao=sqlite3.connect("jogos.db")
                    cursor=conexao.cursor()
                    if filtro!='preco':
                        cursor.execute(f"SELECT * FROM {loja_} WHERE jogo LIKE '%{pesquisa_line}%' order by  {filtro} {order_by};")
                    if filtro=='preco':
                        cursor.execute(f"SELECT * FROM {loja_} WHERE jogo LIKE '%{pesquisa_line}%' order by ORDER BY LENGTH ({filtro}) {order_by};")
                    resultado=cursor.fetchone()
                    print('consulta 2')
                    while True:
                        resultado=cursor.fetchone()
                        if resultado is None:
                            break
                        loja=resultado[0]
                        jogo=resultado[1]
                        preco=resultado[2]
                        pdesconto=resultado[3]
                        poriginal=resultado[4] 
                        linkcompleto=resultado[5] 
                        tipo=resultado[6]
                        data=resultado[7]
                        rowlist_banco.append((loja,data,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                    cursor.close()
                    conexao.close()
                                
                except:
                        print('listra ainda nao criada')
            
    if loja_pesquisa !="Todos" :
                loja_=loja_pesquisa.lower()
                if pesquisa_line=="":
                    try:

                        conexao=sqlite3.connect("jogos.db")
                        cursor=conexao.cursor()
                        if filtro!='preco':
                            cursor.execute(f"select * from {loja_} order by  {filtro} {order_by}")
                        if filtro=='preco':
                            cursor.execute(f"select * from {loja_} ORDER BY LENGTH({filtro}),{filtro}")
                        resultado=cursor.fetchone()
                        while True:
                            resultado=cursor.fetchone()
                            if resultado is None:
                                break
                            loja=resultado[0]
                            jogo=resultado[1]
                            preco=resultado[2]
                            pdesconto=resultado[3]
                            poriginal=resultado[4] 
                            linkcompleto=resultado[5] 
                            tipo=resultado[6]
                            data=resultado[7]
                            rowlist_banco.append((loja,data,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                            #print(loja,data,jogo,preco,pdesconto,poriginal,linkcompleto)
                    
                        cursor.close()
                        conexao.close()
                    except:
                        print('listra ainda nao criada')
                if pesquisa_line!="":
                    try:
                     
                        conexao=sqlite3.connect("jogos.db")
                        cursor=conexao.cursor()
                        if filtro!='preco':
                            cursor.execute(f"SELECT * FROM {loja_} WHERE jogo LIKE '%{pesquisa_line}%' order by  {filtro} {order_by};")
                        if filtro=='preco':
                            cursor.execute(f"SELECT * FROM {loja_} WHERE jogo LIKE '%{pesquisa_line}%' order by ORDER BY LENGTH ({filtro}) {order_by};")
                        resultado=cursor.fetchone()
                       
                        while True:
                            resultado=cursor.fetchone()
                            if resultado is None:
                                break
                            loja=resultado[0]
                            jogo=resultado[1]
                            preco=resultado[2]
                            pdesconto=resultado[3]
                            poriginal=resultado[4] 
                            linkcompleto=resultado[5] 
                            tipo=resultado[6]
                            data=resultado[7]
                            rowlist_banco.append((loja,data,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                        cursor.close()
                        conexao.close()
                                    
                    except:
                            print('listra ainda nao criada')
                
            


