# Dune scoring work

class voter:
    def __init__(self,choice:list,name):
        self.choice = choice
        self.name = name



if __name__ == "__main__":

    import itertools

    factions = {"F", "A","S","E","H"}
    scorepoints = [3,2,1]

    Laura = voter(["F","A","S"],"LA")
    James = voter(["A","E","S"],"JA")
    John  = voter(["S","E","A"],"JO")
    Oli   = voter(["F","S","A"],"OL")
    CallumKate = voter(["S", "H","A"],"CK")

    voters = [Laura, James,John,Oli,CallumKate]



    possibleAssignments = itertools.permutations(factions)
    BestScore = -5
    BestAssignments = []

    for asgn in possibleAssignments:
        score = 0
        for count,factionAssigned in enumerate(asgn):

            if factionAssigned in voters[count].choice:
                score += scorepoints[voters[count].choice.index(factionAssigned)]
            else:
                score -= 1
            

            #print(personAssigned)

        if score > BestScore:
            BestScore = score
            BestAssignments = asgn
        elif score == BestScore:
            print(score)
            print(*asgn)
    print(BestScore)
    print(*BestAssignments)
