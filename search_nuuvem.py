from bs4 import BeautifulSoup 
import re
import requests

rowlistnuuvem=[]
header_nuuvem={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0 (Edition std-1)'}

def nuuvemgame():
    linkjogo='https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/types/games/sort/bestselling/sort-mode/desc/page/1'     
    tipo='Jogo'  
    scrapynuuvem(linkjogo,tipo)  
    linkjogo='https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/types/dlc/sort/bestselling/sort-mode/desc/page/1'
    tipo='DLC'  
    scrapynuuvem(linkjogo,tipo)
    linkjogo='https://www.nuuvem.com/br-pt/catalog/platforms/pc/price/promo/types/package/sort/bestselling/sort-mode/desc/page/1'
    tipo='Pacote'  
    scrapynuuvem(linkjogo,tipo)  
    
def scrapynuuvem(linkjogo,tipo):
    try:
        url_pag= linkjogo
        site= requests.get(url_pag, headers=header_nuuvem, timeout=10)
        soup= BeautifulSoup(site.content,'html.parser')
        qtd_jogo=soup.find('div',class_='products-search-term grid').get_text().strip()
        qtd_jogo=int(qtd_jogo.strip('resultados'))
        jogosporpagina=20
        loja='nuuvem'
        try:
            for i in range(1, (qtd_jogo//jogosporpagina+2)):
                print('NUUVEM:',i)
                url_pag= (f'{linkjogo[:-1]}{i}')
                site= requests.get(url_pag, headers=header_nuuvem, timeout=10)
                soup= BeautifulSoup(site.content,'html.parser')
                produtos= soup.find_all('div',class_= re.compile('product-card--grid'))
                for produto in produtos:
                    try:
                        jogo= produto.find('h3', class_=re.compile('product-title single-line-name')).get_text().strip()
                        pdesconto= produto.find('span', class_=re.compile('product-price--discount')).get_text().strip().replace('-','').replace('%','')
                        preco= produto.find('span', class_=re.compile('product-price--val')).get_text().strip().replace('R$ ','').replace(',','.')
                        link= produto.find('a')#acha a classe do link
                        jok={link.get('href')}#acha o link
                        linkcompleto=(str(jok).strip("{}' "))
                        poriginal=((float(preco)/(100-int(pdesconto)))*100)
                        poriginal="{:.2f}".format(float(poriginal))
                        preco="{:.2f}".format(float(preco))
                        
                        rowlistnuuvem.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                    except:
                        a='x'  
        except:
            a='x'   
    except:
        a='x'      
    