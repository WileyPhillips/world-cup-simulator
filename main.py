# Starting off with teams from the 2014 world cup

teams2014 = ["Brazil", "Mexico", "Croatia", "Cameroon", "Netherlands", "Chile", "Spain", "Australia", "Colombia",
             "Greece", "Ivory Coast", "Japan", "Costa Rica", "Uruguay", "Italy", "England", "France", "Switzerland",
             "Ecuador", "Honduras", "Argentina", "Nigeria", "Bosnia and Herzegovina", "Iran", "Germany", "USA",
             "Portugal", "Ghana", "Belgium", "Algeria", "Russia", "South Korea"]

groups = ["A", "B", "C", "D", "E", "F", "G", "H"]



for i in range(8):
    groupStatement = "group" + groups[i] + " = ["
    for j in range(4):
        if j != 3:
            groupStatement += teams2014[(i*2-1)+j] + ", "
            print((i*2-1)+j)
        else:
            groupStatement = groupStatement[:-1] + " " + teams2014[(i*2-1)+j] +  "]"
            print(groupStatement)


