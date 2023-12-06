from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or, QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

#Tehtävä 4:
    query = QueryBuilder()
    matcher = query.build()                        #1.tapaus: All, number = 1058
    matcher = query.playsIn("NYR").build()          #2. tapaus: plays in "NYR" = 22
    matcher = (                                      #3.tapaus  - And mukaan                                 
        query
        .playsIn("NYR")
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .build()
        )

    for player in stats.matches(matcher):
        print(player)

    #print("Yllä teht 4 tulostus.")

    #Tehtävä 5: 
    matcher2 = (
      query
        .oneOf(
        query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
        query.playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )
        .build()
    )

    #print("Alla teht. 5 tulostus.")   
    for player in stats.matches(matcher2):
        print(player)

    


# Tehtävä 3:
    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(20, "assists"),
    #    PlaysIn("PHI")
    #)

    #for player in stats.matches(matcher):
    #    print(player)
    #print("All")
    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    #for player in stats.matches(matcher):
    #    print(player)

    #print("tulostaa saman kuin yo.")

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    #for player in stats.matches(matcher):
    #    print(player)

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    #print("**Or -testaus**")
    #for player in stats.matches(matcher):
    #    print(player)



    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    #print("**ISO Or -testaus**")
    #for player in stats.matches(matcher):
    #    print(player)





if __name__ == "__main__":
    main()
