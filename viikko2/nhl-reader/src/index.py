import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    players_all = reader.get_players()       #lista Player-olioita
   
    stats = PlayerStats(players_all)
    players = stats.top_scorers_by_nationality("FIN")  #skreenaus kans. mukaan

    for player in players:
        print(player)
    
    #response = requests.get(url).json()  #Tehtävän 11 vastaus 

    ##print("JSON-muotoinen vastaus:")
    #print(response)

    #players = []

    #for player_dict in response:
    #    if player_dict["nationality"] == "FIN":
    #        player = Player(player_dict)
    #        players.append(player)
    #sorted_players = sorted(players, key=lambda x: x.point, reverse = True)
    #print("Players from FIN\n")
    
    #for player in sorted_players: #lisää ehto että jos suomalinen niin printtaa - piti hakea suomalisten tiedot...
    #    print(player)


if __name__ == "__main__":
    main()
