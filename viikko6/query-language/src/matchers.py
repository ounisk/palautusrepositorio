from player_reader import PlayerReader

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    @staticmethod  
    def test(player):
        return True


class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True

        return False
    

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
     
    def test(self, player):
        for matcher in self._matchers:
        #while matcher in self._matchers:
            if matcher.test(player):
                return True
        
        return False    
    
class QueryBuilder:    #tehtävä 4
    #def __init__(self):   #1. tapaus, jossa vain All
    #    self.query_object = All()

    def __init__(self, query = All()):   #2.tapaus, jossa playsIn "NYR"
        self.query_object = query

    #def __init__(self, query = And()):   #3 tapaus, jossa ketjutettuja ehtoja / ei tätät
    #    self.query_object = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query_object,PlaysIn(team)))   #kohtaan #3 yhdistetään hakuja.
        #return QueryBuilder(PlaysIn(team))  # kohtaan #2

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_object, HasAtLeast(value,attr))) 
        #return QueryBuilder(HasAtLeast(value,attr))    # draft versio 

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_object, HasFewerThan(value, attr)))
        #return QueryBuilder(HasFewerThan(value,attr))   #draft versio


    def build(self):
        return self.query_object