import requests
from bs4 import BeautifulSoup as BS

URL = "https://premierliga.ru/tournament-table/"
response = requests.get(URL)
response_txt = response.text
soup = BS(response_txt, 'lxml')
trs = soup.find('div', class_=('stats-tournament-table')).find('table').find_all('tr')
team_list = []
play_statistic_list = []
play_statistic_list_loc = []


def parse_club():
    for tr in trs:
        position = tr.find_all('td', class_='club')
        for i in position:
            positions = i.text
            positionsik = positions.replace('\n', '')
            if positions != '\xa0':
                team_list.append(positionsik)
    return team_list


def parse_point():
    for tr in trs:
        position = tr.find_all('td', class_='dark-blue num')
        for i in position:
            res = i.text
            # print('res',res)
            ressik = res.replace('\n', '')
            if res != '\xa0':
                play_statistic_list_loc.append(ressik)
            play_statistic_list = list(zip(*[iter(play_statistic_list_loc)] * 5))
    return play_statistic_list


def print_results():
    for i in range(len(parse_club())):
        print(i + 1, ' ', parse_club()[i], ' ', parse_point()[i], '\n')


def main():
    print_results()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
