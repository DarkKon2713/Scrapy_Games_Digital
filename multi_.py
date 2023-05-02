import multiprocessing
from search_eshop import*
from search_nuuvem import*
from search_psn import*
from search_steam import*
import sqlite3
from datetime import date
import os
#os.system('cls' if os.name == 'nt' else 'clear')#limpar terminarl





def multi_eshop():
    print("Hello from the new process: Eshop")
    lista='rowlisteshop'
    tabela_='eshop'
    criar_banco(tabela_)
    eshopjogo()
    eshop_assinatura()
    inserir_banco(lista,tabela_)

def multi_nuuvem():
    print("Hello from the new process:Nuuvem")
    lista='rowlistnuuvem'
    tabela_='nuuvem'
    criar_banco(tabela_)
    nuuvemgame()
    inserir_banco(lista,tabela_)

def multi_psn():
    print("Hello from the new process: PSN ")
    lista='rowlistpsn'
    tabela_='psn'
    criar_banco(tabela_)
    psnjogo()
    psn_assinatura()
    inserir_banco(lista,tabela_)

def multi_steam():
    print("Hello from the new process: Steam ")
    lista='rowliststeam'
    tabela_='steam'
    criar_banco(tabela_)
    steam_()
    inserir_banco(lista,tabela_)
    



def inserir_banco(lista,tabela_):
            conexao=sqlite3.connect("jogos.db")
            cursor=conexao.cursor()
            today = date.today()
            data = today.strftime("%d/%m/%Y")
            for r in eval(lista):
                loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo=r
                cursor.execute(f"SELECT * FROM {tabela_} WHERE  loja = ? AND jogo = ? AND preco = ? AND pdesconto = ? AND poriginal = ? AND linkcompleto = ? AND tipo = ? AND data = ?", (loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data))
                linha_existente = cursor.fetchone()
                #print(f'Nome:{nome}\nTipo:{tipo}\nP Original:{preco}\nPromo:{promo}\n%Desc:{percent_}\nLink:{link}')
                if linha_existente is None :
                    cursor.execute(f'''INSERT INTO {tabela_} (loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo,data))
            conexao.commit()
            cursor.close()
            conexao.close()
            print('Inserido na tabela ',loja.upper())
def criar_banco(tabela_):
                try:
                        conexao=sqlite3.connect("jogos.db")
                        cursor=conexao.cursor()
                        
                        cursor.execute(f'''CREATE TABLE {tabela_}
                                (nome TEXT,tipo TEXT,preco TEXT,promo TEXT,percent_ TEXT,link TEXT,data TEXT)''')
                        
                        conexao.commit()
                        cursor.close()
                        conexao.close()
                        print('criou')
                except:
                        pass   
    
if __name__ == '__main__':
    # Start a new process
    p_eshop = multiprocessing.Process(target=multi_eshop)
    p_nuuvem = multiprocessing.Process(target=multi_nuuvem)
    p_psn = multiprocessing.Process(target=multi_psn)
    p_steam = multiprocessing.Process(target=multi_steam)
    p_eshop.start()
    p_nuuvem.start() 
    p_psn.start()
    p_steam.start()
    p_eshop.join()
    p_nuuvem.join() 
    p_psn.join()
    p_steam.join()
    
    

    print("Terminou!")