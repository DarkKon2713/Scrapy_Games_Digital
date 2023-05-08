import requests
import re

link=''
quantidade_paginas=11
formatar_url=''
header_teste={}
post_get='GET'
post=''

header_panini={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Cookie': '_gcl_aw=GCL.1682551999.CjwKCAjwl6OiBhA2EiwAuUwWZcPuNyIYrRrZ4B2-4nr08z6yy_hxUw82GgP-SI-ThfUtaUaNSeKlPRoCF3cQAvD_BwE; _gcl_au=1.1.1852543929.1682551999; _fbp=fb.2.1682551999294.295459718; _gid=GA1.3.951442656.1682551999; _gac_UA-15563537-13=1.1682551999.CjwKCAjwl6OiBhA2EiwAuUwWZcPuNyIYrRrZ4B2-4nr08z6yy_hxUw82GgP-SI-ThfUtaUaNSeKlPRoCF3cQAvD_BwE; _enviou.com-ca={%22tk%22:%2225112020084511ZTT%22}; _lf={%22lm%22:false%2C%22_ga%22:%22c018416b-db06-6337-6fc8-5ac59231975a%22}; Origem=actionpay; form_key=H96umAPvq5koECCD; form_key=H96umAPvq5koECCD; gig_bootstrap_4_IhKfBuvm754xvK7ZKbcg6Q=_gigya_ver4; mage-messages=; amcookie_policy_restriction=allowed; _lfi=3; _lfe=3; PHPSESSID=8e3797c93a1ba0e5ba2382a3a822a3bb; mage-cache-sessid=true; assinatura=false; gig_canary=true; gig_canary_ver=13797-3-28042590; section_data_ids=%7B%22customer%22%3A1682555313%2C%22wishlist%22%3A1682555313%2C%22directory-data%22%3A1682553954%7D; Actionpay=2b48293b-83ea-b15f-d084-0187c01c8908.87274; _ga_5R2YE93QVT=GS1.1.1682551999.1.1.1682555666.60.0.0; _ga=GA1.3.381985515.1682551999; _gat_gtag_UA_15563537_13=1; _dc_gtm_UA-15563537-13=1; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-banners-cache-storage=%7B%7D; _gat_UA-17087845-1=1',
'Host': 'panini.com.br',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0',

}
formatacao_nome=['&#039;'],["'"]

lista_produto_inicio='<ol class="products list items product-items">'
lista_produto_fim='</div><div class="sidebar sidebar-main">'

produto_inicio='<strong class="product name product-item-name"><a class="product-item-link" '
produto_fim='<span>Adicionar para Comparar</span>'

link_inicio='href="'
link_fim='">'

nome_inicio='>'
nome_fim='</a></strong>'

promo_incio='data-price-type="finalPrice" class="price-wrapper " ><span class="price">'
promo_fim='</span></span>  </span></span> <span class="old-price'

preco_inicio='data-price-type="oldPrice" class="price-wrapper " ><span class="price">'
preco_fim='</span></span>  </span></span>  </div> '

link_='https://panini.com.br/ofertas-da-semana?p='
tipo="Manga/HQ"
def scrapy():
    
    for pagina in range(0,quantidade_paginas):
        try:
            link=link_+str(pagina)
            print(link)
            if post_get=="GET":
                if header_teste == {}:
                    site=requests.get(link,timeout=10)
                    
                if header_teste != {}:
                    site=requests.get(link,header=header_teste ,timeout=10)
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