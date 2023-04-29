from bs4 import BeautifulSoup 
import requests 
import json

rowlisteshop=[]
header_eshop={'Accept': '*/*',
'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Origin': 'https://www.nintendo.com',
'Referer': 'https://www.nintendo.com/',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'cross-site',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0 (Edition std-1)',
'content-type': 'application/x-www-form-urlencoded',
'sec-ch-ua': '"Not=A?Brand";v="8", "Chromium";v="110", "Opera GX";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'x-algolia-api-key': 'a29c6927638bfd8cee23993e51e721c9',
'x-algolia-application-id': 'U3B6GR4UA3'}

def eshopjogo():
    
    link='https://u3b6gr4ua3-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser%3B%20JS%20Helper%20(3.11.1)%3B%20react%20(17.0.2)%3B%20react-instantsearch%20(6.38.1)'
    loja='eshop'
    try:
        for j in range(1,1000):
            print('Eshop:',j)
            data_eshop= '{"requests":[{"indexName":"store_game_pt_br","params":"analytics=true&attributesToHighlight=%5B%22description%22%5D&clickAnalytics=true&facetFilters=%5B%22topLevelFilters%3APromo%C3%A7%C3%B5es%22%5D&facetingAfterDistinct=true&facets=%5B%22topLevelFilters%22%2C%22nsoFeatures%22%2C%22corePlatforms%22%2C%22availability%22%2C%22genres%22%2C%22editions%22%2C%22franchises%22%2C%22priceRange%22%2C%22classindRating%22%2C%22playerCount%22%2C%22softwarePublisher%22%2C%22softwareDeveloper%22%5D&filters=(NOT%20objectID%3A7100061846%20AND%20NOT%20objectID%3A7100058797%20AND%20NOT%20objectID%3A7700016945%20AND%20NOT%20objectID%3A7700016946%20AND%20NOT%20objectID%3A7700016943%20AND%20NOT%20objectID%3A7700016942%20AND%20NOT%20objectID%3A7100056956%20AND%20NOT%20objectID%3A7100063709%20AND%20NOT%20objectID%3A7100063714%20AND%20NOT%20objectID%3A7100058128%20AND%20NOT%20objectID%3A7100000153%20AND%20NOT%20objectID%3A7700013723%20AND%20NOT%20objectID%3A7100049936%20AND%20NOT%20objectID%3A7100042934%20AND%20NOT%20objectID%3A7100034439%20AND%20NOT%20objectID%3A7100001620%20AND%20NOT%20objectID%3A7100000734%20AND%20NOT%20objectID%3A7100001130%20AND%20NOT%20objectID%3A7100002722%20AND%20NOT%20objectID%3A7100001339%20AND%20NOT%20objectID%3A7100057046%20AND%20NOT%20objectID%3A7100058802%20AND%20NOT%20objectID%3A7100054892%20AND%20NOT%20objectID%3A7100053336%20AND%20NOT%20objectID%3A7100046400%20AND%20NOT%20objectID%3A7100048000%20AND%20NOT%20objectID%3A7100012332%20AND%20NOT%20objectID%3A7700013808%20AND%20NOT%20objectID%3A7100050787%20AND%20NOT%20objectID%3A7100045182%20AND%20NOT%20objectID%3A7700015577%20AND%20NOT%20objectID%3A7100062434%20AND%20NOT%20objectID%3A7100056360%20AND%20NOT%20objectID%3A7100038380%20AND%20NOT%20objectID%3A7100047561%20AND%20NOT%20objectID%3A7100003816%20AND%20NOT%20objectID%3A7100021364%20AND%20NOT%20objectID%3A7100039856%20AND%20NOT%20objectID%3A7100039333%20AND%20NOT%20objectID%3A7100046395%20AND%20NOT%20objectID%3A7100056620%20AND%20NOT%20objectID%3A7100049931%20AND%20NOT%20objectID%3A7100033556%20AND%20NOT%20objectID%3A7100046405%20AND%20NOT%20objectID%3A7100029237%20AND%20NOT%20objectID%3A7100027619%20AND%20NOT%20objectID%3A7100020033%20AND%20NOT%20objectID%3A7100018694%20AND%20NOT%20objectID%3A7100005302%20AND%20NOT%20objectID%3A7200000061%20AND%20NOT%20objectID%3A7100062478%20AND%20NOT%20objectID%3A7100062483%20AND%20NOT%20objectID%3A7700001541%20AND%20NOT%20objectID%3A7700016659%20AND%20NOT%20objectID%3A7700016660%20AND%20NOT%20objectID%3A7100046983%20AND%20NOT%20objectID%3A7100046988%20AND%20NOT%20objectID%3A7100023176%20AND%20NOT%20objectID%3A7100012879%20AND%20NOT%20objectID%3A7100059877%20AND%20NOT%20objectID%3A7100044948%20AND%20NOT%20objectID%3A7100046999%20AND%20NOT%20objectID%3A7100057985%20AND%20NOT%20objectID%3A7700016683%20AND%20NOT%20objectID%3A7100059676%20AND%20NOT%20objectID%3A7100038144%20AND%20NOT%20objectID%3A7100052943%20AND%20NOT%20objectID%3A7100046189%20AND%20NOT%20objectID%3A7100045037)&highlightPostTag=%5E*&highlightPreTag=%5E*%5E%5E&hitsPerPage=40&page=AQUI&tagFilters="}]}'
            data_eshop=data_eshop.replace('AQUI',str(j))
            match=requests.post(link ,headers=header_eshop,data=data_eshop).json()
            for i in range(0,40):
                match=requests.post(link ,headers=header_eshop,data=data_eshop).json()['results'][0]['hits'][i]
                jogo=match['title']
                preco=match['price']['finalPrice'] 
                poriginal=match['price']['regPrice']
                linkcompleto='https://www.nintendo.com'+match['url']
                pdesconto=f'{int(100-((preco/poriginal)*100))}'
                preco="{:.2f}".format(float(preco))
                poriginal="{:.2f}".format(poriginal)
                if 'DLC' in jogo or 'Style' in jogo or 'Skin' in jogo:
                    tipo='DLC'
                if 'DLC' not in jogo or 'Style' not in jogo or 'Skin' not in jogo:
                    tipo='Jogo'
                if 'Pack' in jogo:
                    tipo='Pack'
                if 'Bundle' in jogo:
                    tipo='Bundle'
                
                rowlisteshop.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
    except:
        print('Pagina max atingido')
