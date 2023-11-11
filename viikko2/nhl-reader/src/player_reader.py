import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()
        #print(response[:5]) #toimii
        players_list = []
        for item in response:  #muodostaa olioita ja lisää ne listaan
            name = item['name']
            nationality = item['nationality']
            team = item['team']
            goals = item['goals']
            assists = item['assists']
            points = item['goals'] + item['assists']

            players_list.append(Player(name, nationality, team, goals, assists, points))  
        
        return players_list