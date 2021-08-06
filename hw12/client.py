import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re



urls = ['https://www.sport-express.ru/live/', 'https://www.championat.com/stat/']




async def parser_voleyball_one(url):
    com = []
    match_statuses = []
    res_home = []
    results_home = []
    res_guest = []
    results_guest = []
    data = []
    async with aiohttp.ClientSession().get(url) as response:

        html = await response.text()
        soup = BeautifulSoup(html, 'lxml')

        
        quotes = soup.find_all('table', class_='match-table--volleyball')

        for q in quotes:

            status = q.find('td', class_='match__status')
            match_statuses.append(status.text)

            comand = q.find_all('td', class_='match__commands--short')
            for c in comand:
                com.append(c.text.strip())

            result_home = q.find('td', class_='match__result--home')
            game_h = []
            res_home_text = result_home.text.strip().replace('\n', ', ')
            if res_home_text:
                game_h.append(res_home_text)
            else:
                game_h.append('0')
            res_home.append(game_h)
    

            result_guest = q.find('td', class_='match__result--guest')
            game_g = []
            res_guest_text = result_guest.text.strip().replace('\n', ', ')
            if res_guest_text:
                game_g.append(res_guest_text)
            else:
                game_g.append('0')
            res_guest.append(game_g)
            
        

        # str to int
        def str_to_int(current_list, new_list):
            for res in current_list:
                for r in res:
                    format_r = r.split(',')
                    for i in range(0, len(format_r)):
                        if format_r[i]:
                            format_r[i] = int(format_r[i])
                    new_list.append(format_r)

        str_to_int(res_home, results_home)
        str_to_int(res_guest, results_guest)


    idx = 1
    for i in range(0, len(com), 2):
        dict_ = {}
        dict_['comand1'] = com[i]
        dict_['comand2'] = com[idx]
        idx += 2
        data.append(dict_)
        dict_ = {}

    index = 0
    for item in data:
        item['status'] = match_statuses[index]
        item['result1'] = results_home[index]
        item['result2'] = results_guest[index]
        index += 1
    

    return data



async def parser_voleyball_second(url):
    data = []
    async with aiohttp.ClientSession().get(url) as response:

        html = await response.text()

        soup = BeautifulSoup(html, 'html.parser')

        matches = soup.find_all('a', href=re.compile("_volleyballog/tournament/.+/match"))
        lists_res = []

        for match in matches:
            lists_res.append(match.text.split(' '))

        for list_res in lists_res:
            dict_ = {}
            for item in list_res:
                if item == '–':
                    dict_['comand1'] = list_res[0]
                    if list_res[1] != item:
                        dict_['comand1'] += ' ' + list_res[1]

                    dict_['comand2'] = list_res[list_res.index(item) + 1]
                    try:
                        if int(list_res[list_res.index(item) + 2]) or int(list_res[list_res.index(item) + 2]) == 0:
                            dict_['result1'] = list_res[list_res.index(item) + 2]
                            dict_['result2'] = list_res[list_res.index(item) + 4]
                    except ValueError:
                        try:
                            dict_['comand2'] += ' ' + list_res[list_res.index(item) + 2]
                        except KeyError:
                            dict_['comand2'] = list_res[list_res.index(item) + 2]
                    except IndexError:
                        continue
                
                
            data.append(dict_)
            dict_ = {}

    return data


async def main():
    parser_one = await parser_voleyball_one(urls[0])
    parser_second = await parser_voleyball_second(urls[1])
    for data_match in parser_second:
        for key, data in data_match.items():
            if key == 'comand1':
                if not any(d['comand1'] == data for d in parser_one):
                    parser_one.append(data_match)

    return parser_one

