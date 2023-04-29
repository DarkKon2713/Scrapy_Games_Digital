import sqlite3
from datetime import date
def inserir_banco(loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo):
    conexao=sqlite3.connect("jogos.db")
    cursor=conexao.cursor()
    today = date.today()
    data = today.strftime("%d/%m/%Y")
    cursor.execute(f"SELECT * FROM {loja} WHERE  loja = ? AND jogo = ? AND preco = ? AND pdesconto = ? AND poriginal = ? AND linkcompleto = ? AND tipo = ? AND data = ?", (loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data))
    linha_existente = cursor.fetchone()
    if linha_existente is None :
        cursor.execute(f'''INSERT INTO {loja} (loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data))
    conexao.commit()
    cursor.close()
    conexao.close()
    