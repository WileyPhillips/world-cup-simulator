import random

# Starting off with teams from the 2014 world cup
teams2014 = ["Brazil", "Mexico", "Croatia", "Cameroon", "Netherlands", "Chile", "Spain", "Australia", "Colombia",
             "Greece", "Ivory Coast", "Japan", "Costa Rica", "Uruguay", "Italy", "England", "France", "Switzerland",
             "Ecuador", "Honduras", "Argentina", "Nigeria", "Bosnia and Herzegovina", "Iran", "Germany", "USA",
             "Portugal", "Ghana", "Belgium", "Algeria", "Russia", "South Korea"]

groups = ["A", "B", "C", "D", "E", "F", "G", "H"]


# the list being used for grouping
groupedList = teams2014


# grouped in order
for i in range(8):
    groupStatement = "group" + groups[i] + " = ["
    for j in range(4):
        if j != 3:
            groupStatement += groupedList[(i*4)+j] + ", "
            print((i*4)+j)
        else:
            groupStatement = groupStatement[:-1] + " " + groupedList[(i*4)+j] +  "]"
            print(groupStatement)


# grouped randomly
for i in range(8):
    groupStatement = "group" + groups[i] + " = ["
    for j in range(4):
        randomTeam = random.randint(0, len(groupedList)-1)
        print(randomTeam)
        if j != 3:
            groupStatement += groupedList[randomTeam] + ", "
            groupedList.pop(randomTeam)
        else:
            groupStatement = groupStatement[:-1] + " " + groupedList[randomTeam] + "]"
            groupedList.pop(randomTeam)
            print(groupStatement)


