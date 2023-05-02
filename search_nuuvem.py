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
    nuuvemgamegift() 
    
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
 
def nuuvemgamegift():
    linkjogo='https://www.nuuvem.com/br-pt/catalog/price/promo/types/giftcard_digital/sort/bestselling/sort-mode/desc/page/1' #promo
    scrapynuuvemgift(linkjogo) 
    linkjogo='https://www.nuuvem.com/br-pt/catalog/types/subscription/sort/bestselling/sort-mode/desc/page/1' #assinaturas  
    scrapynuuvemgift(linkjogo) 
    linkjogo='https://www.nuuvem.com/br-pt/catalog/platforms/playstation/sort/bestselling/sort-mode/desc/page/1' #play
    scrapynuuvemgift(linkjogo) 
    linkjogo='https://www.nuuvem.com/br-pt/catalog/platforms/nintendo/sort/bestselling/sort-mode/desc/page/1' #nintendo
    scrapynuuvemgift(linkjogo) 
    linkjogo='https://www.nuuvem.com/br-pt/catalog/platforms/xbox/sort/bestselling/sort-mode/desc/page/1' #xbox
    scrapynuuvemgift(linkjogo) 
     
    scrapynuuvemgift(linkjogo)  
    

def scrapynuuvemgift(linkjogo):
    try:
        url_pag= linkjogo
        site= requests.get(url_pag, headers=header_nuuvem, timeout=10)
        soup= BeautifulSoup(site.content,'html.parser')
        qtd_jogo=soup.find('div',class_='products-search-term grid').get_text().strip()
        qtd_jogo=int(qtd_jogo.strip('resultados'))
        jogosporpagina=20
        loja='nuuvem'
       
        tipo='GiftCards'
        
        try:
            for i in range(1, (qtd_jogo//jogosporpagina+2)):
                url_pag= (f'{linkjogo[:-1]}{i}')
                site= requests.get(url_pag, headers=header_nuuvem, timeout=10)
                soup= BeautifulSoup(site.content,'html.parser')
                produtos= soup.find_all('div',class_= re.compile('product-card--grid'))
                for produto in produtos:
                    try:
                        x='none'
                        nome= produto.find('div', class_=re.compile('product__available product__purchasable product-card product-card__cover product-btn-add-to-cart--container')).get_text().strip()
                        try:
                            pdesconto= produto.find('span', class_=re.compile('price--discount')).get_text().strip().replace('-','').replace('%','')
                        except:
                            pdesconto=''
                        #preco= produto.find('span', class_=re.compile('product-price--val')).get_text().strip().replace('R$ ','').replace(',','.')
                        link= produto.find('a')#acha a classe do link
                        link={link.get('href')}#acha o link
                        linkcompleto=(str(link).strip("{}' "))
                        nome=nome.replace('\n','')
                        if 'Xbox Live' in nome:
                            jogo=nome[:nome.find('DigitalMicrosoft StoreXbox OneXbox Series S|XR$ ')]
                            preco=nome[len(jogo)+len('DigitalMicrosoft StoreXbox OneXbox Series S|XR$ '):]
                            x='print'
                        elif 'Xbox - Cartão Presente Digital' in nome:
                            jogo=nome[:nome.find('Microsoft StoreWindowsXbox OneXbox Series S|XR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreWindowsXbox OneXbox Series S|XR$ '):]
                            x='print'
                        elif 'Xbox Game Pass Ultimate' in nome:
                            jogo=nome[:nome.find('Microsoft StoreWindowsXbox OneXbox Series S|XR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreWindowsXbox OneXbox Series S|XR$ '):]
                            x='print'
                        elif 'Xbox Game Pass para PC + EA Play -' in nome:
                            jogo=nome[:nome.find('Microsoft StoreWindowsR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreWindowsR$ '):]
                            x='print'
                        elif 'Microsoft StoreWindowsXbox OneXbox Series S|XR$ ' in nome:
                            jogo=nome[:nome.find('Microsoft StoreWindowsXbox OneXbox Series S|XR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreWindowsXbox OneXbox Series S|XR$ '):]
                            x='print'
                            
                        elif 'Microsoft StoreXbox OneXbox Series S|XDLCR$ ' in nome:
                            jogo=nome[:nome.find('Microsoft StoreXbox OneXbox Series S|XDLCR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreXbox OneXbox Series S|XDLCR$ '):]
                            x='print'
                        elif 'Microsoft StoreWindowsXbox OneXbox Series S|XDLCR$ ' in nome:
                            jogo=nome[:nome.find('Microsoft StoreWindowsXbox OneXbox Series S|XDLCR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreWindowsXbox OneXbox Series S|XDLCR$ '):]
                            x='print'
                        elif 'Microsoft StoreXbox OneXbox Series S|XR$ ' in nome:
                            jogo=nome[:nome.find('Microsoft StoreXbox OneXbox Series S|XR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreXbox OneXbox Series S|XR$ '):]
                            x='print'
                        elif 'Microsoft StoreXbox OneR$ ' in nome:
                            jogo=nome[:nome.find('Microsoft StoreXbox OneR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreXbox OneR$ '):]
                            x='print'
                        elif 'WindowsXbox OneR$ ' in nome:
                            jogo=nome[:nome.find('WindowsXbox OneR$ ')]
                            preco=nome[len(jogo)+len('WindowsXbox OneR$ '):]
                            x='print'
                        elif 'Microsoft StoreWindowsXbox Series S|XR$ ' in nome:
                            jogo=nome[:nome.find('Microsoft StoreWindowsXbox Series S|XR$ ')]
                            preco=nome[len(jogo)+len('Microsoft StoreWindowsXbox Series S|XR$ '):]
                            x='print'
                        #--------------------------------------------------------------------
                        elif 'Nintendo eShopNintendo SwitchDLCR$ ' in nome:
                            jogo=nome[:nome.find
                                      ('Nintendo eShopNintendo SwitchDLCR$ ')]
                            preco=nome[len(jogo)+len('Nintendo eShopNintendo SwitchR$ '):]
                            x='print'
                        elif 'Nintendo - Gift Card Digital' in nome:
                            jogo=nome[:nome.find('Nintendo eShopNintendo SwitchR$')]
                            preco=nome[len(jogo)+len('Nintendo eShopNintendo SwitchR$ '):]
                            x='print'
                        
                        elif 'MesesNintendo' in nome:
                            jogo=nome[:nome.find('Nintendo eShopNintendo SwitchR$ ')]
                            preco=nome[len(jogo)+len('Nintendo eShopNintendo SwitchR$ '):]
                            x='print'
                        elif 'Nintendo eShopNintendo SwitchR$ 'in nome:
                            jogo=nome[:nome.find('Nintendo SwitchR$ ')]
                            preco=nome[len(jogo)+len('Nintendo SwitchR$ '):]
                            x='print'
                        
                        #--------------------------------------------------------------------   
                        elif 'Playstation StorePlayStation 4PlayStation 5R$' in nome:
                            jogo=nome[:nome.find('Playstation StorePlayStation 4PlayStation 5R$')]
                            preco=nome[len(jogo)+len('Playstation StorePlayStation 4PlayStation 5R$ '):]
                            x='print'
                        #--------------------------------------------------------------------   
                        elif 'DigitalGoogle' in nome:
                            jogo=nome[:nome.find('DigitalGoogle')]
                            preco=nome[len(jogo)+len(' - Gift Card DigitalGoogle Play StoreAndroidR$ '):]
                            x='print'
                        #--------------------------------------------------------------------   
                        elif 'WindowsAndroidiOSLinuxmacOSR$ ' in nome:
                            jogo=nome[:nome.find('WindowsAndroidiOSLinuxmacOSR$ ')]
                            preco=nome[len(jogo)+len('WindowsAndroidiOSLinuxmacOSR$  '):]
                            x='print'
                        elif 'AndroidiOSLinuxmacOSR$' in nome:
                            jogo=nome[:nome.find('AndroidiOSLinuxmacOSR$')]
                            preco=nome[len(jogo)+len('AndroidiOSLinuxmacOSR$ '):]
                            x='print'
                        

                        if x=='print':
                            
                            poriginal=preco
                            preco=''
                            if 'R$' in poriginal:
                                poriginal=poriginal.replace('R$','')
                            rowlistnuuvem.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                    except:
                        print('nao achou') 
        except:
            a='x'   
    except:
        a='x'      
