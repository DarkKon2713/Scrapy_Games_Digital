import requests 

rowlistpsn=[]
headers_psn={'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
'apollographql-client-name': '@sie-ppr-web-store/app',
'apollographql-client-version': '@sie-ppr-web-store/app@0.73.0',
'content-type': 'application/json',
'cookie': 's_fid=34AD2F686DF7F6D4-225E2FC98AE1E621; s_cc=true; AMCVS_BD260C0F53C9733E0A490D45%40AdobeOrg=1; s_ecid=MCMID%7C01319760329794744191023826203391196295; at_check=true; _evga_9736={%22uuid%22:%2228bbab4c22f0f358%22}; _sfid_c0f4={%22anonymousId%22:%2228bbab4c22f0f358%22%2C%22consents%22:[]}; _gcl_au=1.1.1908992922.1679333356; AMCV_BD260C0F53C9733E0A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C19441%7CMCMID%7C01319760329794744191023826203391196295%7CMCAAMLH-1680292108%7C4%7CMCAAMB-1680292108%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1679694508s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; mbox=PC#3cc6d24c90f5488ab2ed80109283ceaa.35_0#1742578156|session#68a8116b9e274f9683410ef748861695#1679689200; da_lid=102E88B99A7DEA0B2582BB99F1542374D4|0|0|0; s_sq=%5B%5BB%5D%5D; bm_sz=EF33B5A9334E1FC34609D96E89644C44~YAAQNOk7F5MLhBOHAQAAnnqOLRNMpGDkMmS0rvsWJbWST+ysh89Xuqxy3CEQBLFylysRHofIpSbl5GLTMAh7yTam32J/e8ODFQQFVMTk77oirlHy9z1bLnHAywa5qu7KDoTSaR/7TNCmN/KGHU18u348GFL8Q+D8of/p99FgLdjtQ8OrKFkwNmsD3lGOMdFBenhzNVPYQXwJIb9EOFvkOhloyP3EQcQcxdG/XI7y2bkIB056vh54f/SlDbNsfvXFN6e4A2j49iLDaDqLTFvrXD2VaGXNAKEK03IRP+P4mzlrDiH0Dh7EOjLkO25nwkhi5niviN78/ClKT2ken5buVjGL+yCV+2qKOimEpG0hQtAF5KMkmbdu9UmVztfiq/kmYq6opxvPwu1HtWWnUtOY8s1uawm9wESmzK4/E6ciP4rCBF8M47dh2jncz5LoADF333WtjAJuXuARkeKcGNQino+0yg+395cJebUV5d7RB528DGurza5PnAHlRVmkxoyta0Vtthr3FF4VDLo4FGz0zyWeFzK2PNy59Jlpe5Mb6tUwNSWlNaEkBJ8=~3163190~3555632; _abck=9B1D00C3BFE8B85122F47ABCC79839FE~-1~YAAQDOk7F0XBnROHAQAA0w+PLQl1Ggpc5wB6pAHgUl7rqs9EpvTfXY+nd8N089Rcc0aySo4Ng9hZGRJVDtL7dDIf1wxTORL8dgrgriO/tJ/wVzCn7P3ab8IwSyM3IqGW7BBt9T2ZVh5GUNt0d1x62QSA1IxCfDAMtWlWj4BtAONBslp5dKy4ntvy/HFCDnvAear5gKCJTHc97WNPozeiXaYMWm1ZPkvHWKRmEsyoJKlw1r4zuLPobJMd/pf+EmF9Uz7qhtelKKUtw2UhqSvgthx+oXJeH/HRwcsBnKBggeEFMqBIZhs0BcfeLmDMGFn01fe982zNFhBH2E4U6h9vfYIyJ7HyacO2gFAYHMn0+wnqBDt6B26G7cfiOicGdAzR3dotOFY4G53jOnAKmRlnLFjVOkSRagIpvHrtKDPFwlIUgGk20b6pATEg3VbmHXhiLJytOFETr0l4thdSbWCMPQPWsg/6wV9MU+riB8K7+wb7Arho~-1~-1~-1',
'origin': 'https://store.playstation.com',
'referer': 'https://store.playstation.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Safari/537.36',
'x-psn-app-ver': '@sie-ppr-web-store/app/@sie-ppr-web-store/app@0.73.0-c7815359c8ba5c8a5528f80ef27f4c59dd11f706',
'x-psn-correlation-id': '8092cf0a-c354-46cf-957a-c77b24ef4d00',
'x-psn-request-id': 'ea344272-9af4-48bd-ae6a-c74804e80de7',
'x-psn-store-locale-override': 'pt-BR',}
def psnjogo():
    link=f'https://web.np.playstation.com/api/graphql/v1//op?operationName=categoryGridRetrieve&variables=%7B%22id%22%3A%2235027334-375e-423b-b500-0d4d85eff784%22%2C%22pageArgs%22%3A%7B%22size%22%3A24%2C%22offset%22%3A24%7D%2C%22sortBy%22%3Anull%2C%22filterBy%22%3A%5B%5D%2C%22facetOptions%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35%22%7D%7D'
    nav=requests.get(link ,headers=headers_psn)
    pesquisa=nav.json()
    qtdjogos=pesquisa["data"]["categoryGridRetrieve"]['pageInfo']['totalCount']
    jogos_por_pagina=24 
    limite_json=1000
    paginas=qtdjogos//limite_json
    jogo_atual=1
    
    if paginas ==0:#offset é o inicio e size o tamanho 
        offset=0
        if qtdjogos<=jogos_por_pagina:#menos de 24 jogos
            size=jogos_por_pagina
            request_psn(offset,size,qtdjogos,jogo_atual)              
        else:
            size=(qtdjogos//jogos_por_pagina)*jogos_por_pagina
            request_psn(offset,size,qtdjogos,jogo_atual)
    elif paginas >=1:
        for i in range(1,paginas+1):
            size=limite_json
            offset=(limite_json+1)*(i-1)
            request_psn(offset,size,qtdjogos,jogo_atual)
        if qtdjogos%limite_json >=1:
            size=qtdjogos%limite_json
            offset=(qtdjogos-size)+1
            request_psn(offset,size,qtdjogos,jogo_atual)
    
    
        
def request_psn(offset,size,qtdjogos,jogo_atual):
    
    loja='psn'
    link=f'https://web.np.playstation.com/api/graphql/v1//op?operationName=categoryGridRetrieve&variables=%7B%22id%22%3A%2235027334-375e-423b-b500-0d4d85eff784%22%2C%22pageArgs%22%3A%7B%22size%22%3A{size}%2C%22offset%22%3A{offset}%7D%2C%22sortBy%22%3Anull%2C%22filterBy%22%3A%5B%5D%2C%22facetOptions%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%224ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35%22%7D%7D'
    nav=requests.get(link,headers=headers_psn)
    pesquisa=nav.json()
    try:
        for conteudo_jogo in pesquisa["data"]["categoryGridRetrieve"]["products"]:
            
            jogo=conteudo_jogo['name']
            linkcompleto=f"https://store.playstation.com/pt-br/product/{conteudo_jogo['id']}"
            poriginal=conteudo_jogo['price']['basePrice'].replace('R$','').replace(',','.')
            try:
                pdesconto=conteudo_jogo['price']['discountText'].replace('-','').replace('%','')
            except:
                pdesconto=None
            preco=conteudo_jogo['price']['discountedPrice'].replace('R$','').replace(',','.')
            tipo=conteudo_jogo['localizedStoreDisplayClassification']
            
            if preco!="Indisponível" and preco!="Gratuito" and pdesconto != None:
                
                rowlistpsn.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                
    except:
        print("error")



        
def psn_assinatura():
    links=['https://web.np.playstation.com/api/graphql/v1/op?operationName=featuresRetrieve&variables=%7B"tierLabel"%3A"TIER_10"%7D&extensions=%7B"persistedQuery"%3A%7B"version"%3A1%2C"sha256Hash"%3A"010870e8b9269c5bcf06b60190edbf5229310d8fae5b86515ad73f05bd11c4d1"%7D%7D'
,'https://web.np.playstation.com/api/graphql/v1/op?operationName=featuresRetrieve&variables=%7B"tierLabel"%3A"TIER_20"%7D&extensions=%7B"persistedQuery"%3A%7B"version"%3A1%2C"sha256Hash"%3A"010870e8b9269c5bcf06b60190edbf5229310d8fae5b86515ad73f05bd11c4d1"%7D%7D'
,'https://web.np.playstation.com/api/graphql/v1/op?operationName=featuresRetrieve&variables=%7B"tierLabel"%3A"TIER_30"%7D&extensions=%7B"persistedQuery"%3A%7B"version"%3A1%2C"sha256Hash"%3A"010870e8b9269c5bcf06b60190edbf5229310d8fae5b86515ad73f05bd11c4d1"%7D%7D']
    plano=['ESSENCIAL','EXTRA ','DELUXE ']
    assinaturas=['1 mes','3 meses','12 meses'] 
    loja='psn'
    tipo='Assinatura'
    linkcompleto='https://www.playstation.com/pt-br/ps-plus/#subscriptions'
    for link in enumerate(links):
        
        for assinatura in enumerate(assinaturas):
            nav=requests.get(link[1] ,headers=headers_psn)
            pesquisa=nav.json()
            pesquisa=pesquisa['data']['tierSelectorOffersRetrieve']['offers'][assinatura[0]]
            tempo=pesquisa['title'].replace('Assinatura de','')
            poriginal=pesquisa['price']['basePrice']
            preco=pesquisa['price']['discountedPrice']
            jogo=plano[link[0]]+tempo
            if poriginal!=preco:
                pdesconto=f'{int(100-((preco/poriginal)*100))}'
                preco=preco.replace('R$','').replace(',','.')
            if poriginal==preco:
                preco=''
                pdesconto=''
                poriginal=poriginal.replace('R$','').replace(',','.')
               
            rowlistpsn.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
