from bs4 import BeautifulSoup 
import re
from time import sleep
import requests 
import json

rowliststeam=[]
header_steam={'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Cookie': 'browserid=2976354983612813942; timezoneOffset=-10800,0; _ga=GA1.2.148204254.1678362103; lastagecheckage=1-0-1969; sessionid=1be161785d684f9b28f92c81; birthtime=-34199999; steamCountry=BR%7Ca5ebd2db65326c28abb942eb65f7de68; steamLoginSecure=76561198199188373%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQyMF8yMjNBOUExQl8yMjM0MSIsICJzdWIiOiAiNzY1NjExOTgxOTkxODgzNzMiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4MDI4NDY2OSwgIm5iZiI6IDE2NzE1NTY3MzgsICJpYXQiOiAxNjgwMTk2NzM4LCAianRpIjogIjE3RTVfMjI0RThCMzJfNzIzMUIiLCAib2F0IjogMTY3OTA4MzM4MywgInJ0X2V4cCI6IDE2OTc0MTM5MDEsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxNzkuMTUyLjUyLjEwMCIsICJpcF9jb25maXJtZXIiOiAiMTc5LjE1Mi41Mi4xMDAiIH0.kncIaWGxJir76GY9atmhAwgB7z2Pi8dGQ2265u_C2I4yzUktDOL75gGNapV06r8AvDECoMDhC9PW8wJdH3-zCg; _gid=GA1.2.715742366.1680196740; recentapps=%7B%22991560%22%3A1680207452%2C%22799600%22%3A1680207408%2C%221811260%22%3A1679085434%2C%22730%22%3A1679085431%2C%22377600%22%3A1679082190%2C%22312750%22%3A1679082164%2C%221237320%22%3A1678997042%2C%221592500%22%3A1678362316%2C%2239210%22%3A1678362165%7D; app_impressions=19680@1_7_7_2300_150_2|774171@1_7_7_2300_150_2|1211600@1_7_7_2300_150_2|502500@1_7_7_2300_150_2|1262240@1_7_7_2300_150_2|1120320@1_7_7_2300_150_2|1462570@1_7_7_2300_150_2|2177430@1_7_7_2300_150_2|1760250@1_7_7_2300_150_2|47810@1_7_7_2300_150_2|17390@1_7_7_2300_150_2|915810@1_7_7_2300_150_2|606880@1_7_7_2300_150_2|1730590@1_7_7_2300_150_2|755500@1_7_7_2300_150_1|454650@1_7_7_2300_150_1|678950@1_7_7_2300_150_1|728880@1_7_7_2300_150_1|457140@1_7_7_2300_150_1|1244460@1_7_7_2300_150_1|1692250@1_7_7_2300_150_1|1238810@1_7_7_2300_150_1|1328670@1_7_7_2300_150_1|2138710@1_7_7_2300_150_1|768200@1_7_7_2300_150_1|1551360@1_7_7_2300_150_1|1811260@1_7_7_2300_150_1|1190000@1_7_7_2300_150_1|1466060@1_7_7_2300_150_1|1922560@1_7_7_2300_150_1|1222690@1_7_7_2300_150_1|1096530@1_7_7_2300_150_1|1169040@1_7_7_2300_150_1|699130@1_7_7_2300_150_1|1274570@1_7_7_2300_150_1|1929610@1_7_7_2300_150_1|581320@1_7_7_2300_150_1|1121560@1_7_7_2300_150_1|1426210@1_7_7_2300_150_1|1238860@1_7_7_2300_150_1|1238840@1_7_7_2300_150_1|508440@1_7_7_2300_150_2|1372110@1_7_7_2300_150_1|1657630@1_7_7_2300_150_1|1402120@1_7_7_2300_150_1|433340@1_7_7_2300_150_1|1237970@1_7_7_2300_150_1|477160@1_7_7_2300_150_1|12200@1_7_7_2300_150_1|1238040@1_7_7_2300_150_1|1238000@1_7_7_2300_150_1|1580790@1_7_7_2300_150_1|204100@1_7_7_2300_150_1|361420@1_7_7_2300_150_1|1452490@1_7_7_2300_150_1',
'Host': 'store.steampowered.com',
'Referer': 'https://store.steampowered.com/search/?specials=1&ndl=1',
'sec-ch-ua': '"Not=A?Brand";v="8", "Chromium";v="110", "Opera GX";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0 (Edition std-1)',
'X-Prototype-Version': '1.7',
'X-Requested-With': 'XMLHttpRequest'}
def steam_():
        try:
            link_steam='https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&force_infinite=1&specials=1&ndl=1&snr=1_7_7_2300_7&infinite=1'
            match=requests.get(link_steam ,headers=header_steam).json()
            quantidade=int(match['total_count'])
            jogos_por_pagina=100
            paginas=quantidade//jogos_por_pagina
            if quantidade%jogos_por_pagina >=1:
                paginas=paginas+1
            for i in range(1,paginas+1):
                start=(i-1)*jogos_por_pagina
                print('STEAM:',i)
                link_pesquisa=f'https://store.steampowered.com/search/results/?query&start={start}&count=100&dynamic_data=&force_infinite=1&specials=1&ndl=1&snr=1_7_7_2300_7&infinite=1'
                search_steam(link_pesquisa)
        except:
             print('steam fora do ar')
def search_steam(link_pesquisa):
        loja='steam'
        match=requests.get(link_pesquisa ,headers=header_steam).json()
        regex_href='href="(.*)" onmouseout'
        if match:
            results_html = match['results_html']
            #
            # results_html)
            soup= BeautifulSoup(results_html,'html.parser')
            produtos=soup.findAll('a',{'class':['search_result_row ds_collapse_flag']})
            for produto in produtos:
                jogo=produto.find('span',class_='title').get_text()
                pdesconto= produto.find('div', class_='col search_discount responsive_secondrow').get_text().replace('-','').replace('\n','')
                try:
                    preco= produto.find('div', class_='col search_price discounted responsive_secondrow').get_text()
                    x=preco[3:].find('R$ ')
                    poriginal=preco[:x+3].replace('\n','').replace('R$ ','').replace(',','.')
                    preco=preco[x+3:].replace('\n','').replace('R$ ','').replace(',','.')
                    
                except:
                    preco="nao achou"   
                linkcompleto=re.search(regex_href,str(produto)).group(1)
                linkcompleto=linkcompleto[:linkcompleto.find('/?snr=')]
                if 'DLC' in jogo or 'Style' in jogo or 'Skin' in jogo:
                    tipo='DLC'
                if 'DLC' not in jogo or 'Style' not in jogo or 'Skin' not in jogo:
                    tipo='Jogo'
                if 'Pack' in jogo:
                    tipo='Pack'
                if 'Bundle' in jogo:
                    tipo='Bundle'
                if '%' in pdesconto:
                    
                    pdesconto=pdesconto.replace('%','')
                    rowliststeam.append((loja,jogo,preco,pdesconto,poriginal,linkcompleto,tipo))
                    
         