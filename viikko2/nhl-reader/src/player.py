class Player:
    def __init__(self, name, nationality, team, goals, assists, points): 
        self.name = name 
        self.nationality = nationality 
        self.team = team 
        self.goals = goals 
        self.assists = assists 
        self.point = points

    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return (f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.points}")
