from bs4 import BeautifulSoup
from fastapi import Depends
from models import Comand

import requests


url1 = 'https://terrikon.com/football/ukraine/championship/'
url2 = 'https://football.ua/ukraine/table.html'


def get_soup(url_adress):
    response = requests.get(url_adress)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_data_first(url1):
    soup = get_soup(url1)
    tr_list = soup.find('table', class_='grouptable').find_all('tr')
    data_list = []
    for tr in tr_list[1:]:
        data_dict = {}
        data_dict['rating'] = int(tr.find('td').string[:-1])
        data_dict['name'] = tr.find('a').contents[1].strip()
        data_dict['games'] = int(tr.find('td', class_='team').next_sibling.string)
        data_dict['wins'] = int(tr.find('td', class_='win').string)
        data_dict['draws'] = int(tr.find('td', class_='draw').string)
        data_dict['losses'] = int(tr.find('td', class_='lose').string)
        data_dict['goals_in'] = int(tr.find('td', class_='lose').next_sibling.string)
        data_dict['goals_out'] = int(tr.find('td', string='-').next_sibling.string)
        data_dict['scores'] = int(tr.find('strong').string)
        
        data_list.append(data_dict)

    return data_list


def get_data_second(url2):
    soup = get_soup(url2)
    tr_list = soup.find('table', class_='main-tournament-table').find_all('tr')
    data_list = []

    for tr in tr_list[1:]:
        data_dict = {}
        data_dict['rating'] = int(tr.find('td', class_='num').string)
        data_dict['logo'] = tr.find('td', class_='logo').img.get('src')
        data_dict['name'] = tr.find('td', class_='team').get_text().strip()
        data_dict['games'] = int(tr.find('td', class_='games').get_text())
        data_dict['wins'] = int(tr.find('td', class_='win').get_text())
        data_dict['draws'] = int(tr.find('td', class_='draw').get_text())
        data_dict['losses'] = int(tr.find('td', class_='lose').get_text())
        data_dict['goals_in'] = int(tr.find('td', class_='goal').get_text())
        data_dict['goals_out'] = int(tr.find('td', class_='miss').get_text())
        data_dict['difference'] = int(tr.find('td', class_='diff').get_text())
        data_dict['scores'] = int(tr.find('td', class_='score').get_text())

        data_list.append(data_dict)

    return data_list


def add_commands_to_db(db):
    data_first = get_data_first(url1)
    data_second = get_data_second(url2)

    for i in range(len(data_first)):
        data_first[i].update(data_second[i])

        db_comand = Comand(
        rating = data_first[i]['rating'],
        logo = data_first[i]['logo'],
        name = data_first[i]['name'],
        games = data_first[i]['games'],
        wins = data_first[i]['wins'],
        draws = data_first[i]['draws'],
        losses = data_first[i]['losses'],
        goals_in = data_first[i]['goals_in'],
        goals_out = data_first[i]['goals_out'],
        difference = data_first[i]['difference'],
        scores = data_first[i]['scores']
        )

        name = data_first[i]['name']
        
        if not db.query(Comand).filter(Comand.name == name).first():
            db.add(db_comand)
            db.commit()
            db.refresh(db_comand)
        
    return db.query(Comand).all()

