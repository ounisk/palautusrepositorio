class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.point = dict['goals'] + dict['assists']

    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return (f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.points}")
