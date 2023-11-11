from player_reader import PlayerReader, Player
from player import Player


class PlayerStats:
    def __init__(self, response):
        self._response = response   #eli tulee lista Player-olioita

    def top_scorers_by_nationality(self, national):
        players = []

        for player in self._response:

            if player.nationality == national: #Tsekataan vastaako kansalaisuus mitä halutaan
            #if self._response.nationality == national: #
                #print("suomalainen") #toimii    
                #print(player) #toimii
                players.append(player)

        sorted_players = sorted(players, key=lambda x: x.point, reverse = True)
        return sorted_players
