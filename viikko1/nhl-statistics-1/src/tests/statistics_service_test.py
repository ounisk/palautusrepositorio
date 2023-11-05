import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player(self): #, name):
        player = self.stats.search("Kurri")
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_search_unknown_player(self):
        player = self.stats.search("Tikkanen")
        self.assertEqual(player, None )
    
    def test_team_players(self):
        team = self.stats.team("PIT")
        self.assertEqual(str(team[0]), "Lemieux PIT 45 + 54 = 99")

    def test_sorted_players(self):
        sorted = self.stats.top(1)
        self.assertEqual(str(sorted[0]), "Gretzky EDM 35 + 89 = 124") #  top player

    def test_sorted_players_points(self):
        sorted_points = self.stats.top(4, SortBy.POINTS) 
        self.assertEqual(str(sorted_points[1]), "Lemieux PIT 45 + 54 = 99") # pisteiden mukaan 2.

    def test_sorted_players_goals(self):
        sorted_goals = self.stats.top(4, SortBy.GOALS) 
        self.assertEqual(str(sorted_goals[0]), "Lemieux PIT 45 + 54 = 99") #maalien mukaan 1.

    def test_sorted_players_assists(self):
        sorted_assists = self.stats.top(4, SortBy.ASSISTS) 
        self.assertEqual(str(sorted_assists[0]), "Gretzky EDM 35 + 89 = 124") #syöttejen mukaan 1.