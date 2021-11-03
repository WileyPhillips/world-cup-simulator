import random

global groups

# Starting off with teams from the 2014 world cup
teams2014 = ["Brazil", "Mexico", "Croatia", "Cameroon", "Netherlands", "Chile", "Spain", "Australia", "Colombia",
             "Greece", "Ivory Coast", "Japan", "Costa Rica", "Uruguay", "Italy", "England", "France", "Switzerland",
             "Ecuador", "Honduras", "Argentina", "Nigeria", "Bosnia and Herzegovina", "Iran", "Germany", "USA",
             "Portugal", "Ghana", "Belgium", "Algeria", "Russia", "South Korea"]

groupLetter = ["A", "B", "C", "D", "E", "F", "G", "H"]


# the list being used for grouping
groupedList = teams2014
groups = []

# grouped in order
def orderGroup():
    global groups
    groups = []
    for i in range(8):
        groups.append([])
        for j in range(4):
            groups[-1].append(groupedList[(i*4)+j])
    print(groups)


# grouped randomly
def randomGroup():
    global groups
    groups = []
    for i in range(8):
        groups.append([])
        for j in range(4):
            randomTeam = random.randint(0, len(groupedList)-1)
            groups[-1].append(groupedList[randomTeam])
            groupedList.pop(randomTeam)
    print(groups)


def generateMatches():
    print(groups)
    matches = []
    # Will create 8 lists inside the matches list
    # One for each group
    for i in range(8):
        matches.append([])
        # For the group being worked on it creates a list for each team in the group and their matches
        matches[i].append([groups[i][1], groups[i][2], groups[i][3]])
        matches[i].append([groups[i][0], groups[i][3], groups[i][2]])
        matches[i].append([groups[i][3], groups[i][0], groups[i][1]])
        matches[i].append([groups[i][2], groups[i][1], groups[i][0]])
    print(matches)




orderGroup()
randomGroup()
generateMatches()
