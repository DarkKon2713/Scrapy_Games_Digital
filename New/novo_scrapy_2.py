import requests
import re
from bs4 import BeautifulSoup
link=''
quantidade_paginas=20
formatar_url=''
header_loja={
    
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Cookie': 'store_login_session=7eb84de96b20d745a41602a7769b9bb79153277a%7ECJwxap6FxH9iSX0XRn1hwmrJKo7O1Z3EQDgZiIpt; _gid=GA1.3.108842909.1682605854; _fbp=fb.2.1682605854211.1578084550; _gcl_au=1.1.68302507.1682605854; tn_track=a3e7c7423870a494a4a3a82ee3a6d7509dbdd21e%7E28beb77054ab49e3014ef774430287ca; tn_tracksession=4568e18261c30b8d72161c487a2e6e4e0b5cc8e4%7E05c4425d2f033e10ea186191dee28634; __cfruid=08ae3af3002036286915a2f0f2e1db93bd9bd0ed-1682605872; cookie_consent=1; _gat=1; _ga=GA1.1.2086965564.1682605854; store_session_payload_2079231=5fe64a30720c9cbad25a1b9cdce06682aa26728d%7EtnIdFBsytpLAu%2BoMVCFRBsrdlauILkUyRn%2BN0CewwaFzI%2Fa8c88uyMIEH5q0VYUWBQllL4U6DUIhZi%2Byr%2FeHHSXCdo4CfjctroxKsd47vDMu3ha8I8jFzBGFcwZP%2FD1E2qZRhnfV2iilMX%2ByxsPdmvKMwABDSNg%2BXn0uwPRs4i7wOjMveJbV0fXvpsPP5EIOV7k6UbZPeeIGtRu8Fu4XVwsMhfGn%2BshKlRaBfPxPMpwAoNMGDHICxeB7tFv7ZDbnbALRhwGqyJ4XGdof5EG2lSRp7MQ%2BP%2Fm66X03bopuAffRGkl7LZCWmoDZXvBQuC3xxpLaF%2F5CRjHKgxABQDRSxA%3D%3D; _ga_L66SPHD8D2=GS1.1.1682605853.1.1.1682606309.0.0.0',

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0 (Edition std-1)',

}
post_get='GET'
post=''


formatacao_nome=['&#039;'],["'"]

lista_produto_inicio='<div class="col" data-store="category-grid-13301223">'
lista_produto_fim='<div class="text-center mt-5 mb-5">'

produto_inicio='class="js-item-product  col-6 col-md-4 col-lg-3"'
produto_fim=' <span class="d-none d-md-inline-block">Espiar</span></a>'

link_inicio='<a href="'
link_fim='" title="'

nome_inicio='" title="'
nome_fim='" aria-label="'

promo_incio=',&quot;price_short&quot;:&quot;'
promo_fim='&quot;,&quot;price_long&quot;:&quot;'

preco_inicio='&quot;,&quot;compare_at_price_long&quot;:&quot;'
preco_fim='&quot;,&quot;compare_at_price_number&quot;:'

link_='https://www.lojanerdz.com.br/promocoes/?page='
tipo="Manga/HQ"
def scrapy():
    
    for pagina in range(1,quantidade_paginas):
        try:
            link=link_+str(pagina)
            print(link)
            if post_get=="GET":
                if header_loja == {}:
                    print(post_get,'sem header')
                    site=requests.get(link,timeout=10)
                    
                    
                if header_loja != {}:
                    print(post_get,'com header')
                    site= requests.get(link, header_loja, timeout=10)
                    soupe= BeautifulSoup(site.content,'html.parser')
                    
            if post_get=="POST":
                print('Post')

            status=site
            print(status)
            conteudo_site=site.text
            conteudo_produtos=conteudo_site[conteudo_site.find(lista_produto_inicio):conteudo_site.find(lista_produto_fim)]
            #posiçoes de inicio do produto
            produto_=produto_inicio
            posicoes_inicio=repticao_produtos(conteudo_produtos,produto_)
            #print(posicoes_inicio)
            produto_=produto_fim
            posicoes_fim=repticao_produtos(conteudo_produtos,produto_)
            #print(posicoes_fim)
            if len(posicoes_inicio)==len(posicoes_fim):
                for i in range(0,len(posicoes_fim)):
                    produto=conteudo_produtos[posicoes_inicio[i]+len(produto_inicio):posicoes_fim[i]]
                    nome=produto[produto.find(nome_inicio)+len(nome_inicio):produto.find(nome_fim)]
                    link_promo=produto[produto.find(link_inicio)+len(link_inicio):produto.find(link_fim)]
                    try:
                        promo=produto[produto.find(promo_incio)+len(promo_incio):produto.find(promo_fim)]
                    except:
                        promo=produto[produto.find(promo_incio)+len(promo_incio):]
                        promo=promo[:produto.find(promo_fim)]
                    try:
                        preco=produto[produto.find(preco_inicio)+len(preco_inicio):produto.find(preco_fim)]
                    except:
                        preco=produto[produto.find(preco_inicio)+len(preco_inicio):]
                        preco=preco[:produto.find(preco_fim)]
                    if 'R$' in promo and preco:
                        promo=promo.replace('R$','')
                        preco=preco.replace('R$','')
                    if ',' in promo and preco:
                        promo=promo.replace(',','.')
                        preco=preco.replace(',','.')
                    try:
                        for j in range(0, len(formatacao_nome)):
                            if formatacao_nome[0][j] in nome:
                                nome=nome.replace(formatacao_nome[0][j],formatacao_nome[1][j])
                    except:
                        pass
                        
                    percent_=int(100-((float(promo)/float(preco))*100))
                    print(nome,link_promo,promo,preco,percent_)
        except:
            break
        
def repticao_produtos(conteudo_produtos,produto_):
    padrao = re.escape(produto_)  
    resultados = re.finditer(padrao, conteudo_produtos)
    posicoes= [match.start() for match in resultados]
    return posicoes
scrapy()