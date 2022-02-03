#data = '5483143223,2745854711,5264556173,6141336146,6357385478,4167524645,2176841721,6882881134,4846848554,5283751526'.split(',')
data = '6318185732,1122687135,5173237676,8754362612,5718474666,8443654137,1247634346,1446514585,6717288267,1727871228'.split(',')
grid = {}
for y, row in enumerate(data):
    for x, energyLevel in enumerate(row):
        grid[(x, y)] = int(energyLevel)

def displayGrid(g):
    for y in range(10):
        for x in range(10):
            sep = ''
            if g[(x, y)] > 9:
                sep = '|'
            print(sep + str(g[(x, y)]) + sep, end='')
        print()
    print()

def nextStepGrid(g):
    # Increment for the simulation step:
    for x in range(10):
        for y in range(10):
            g[(x, y)] = g[(x, y)] + 1


    numFlashes = 0
    while True:
        atLeastOneNeighborFlashed = False
        for x in range(10):
            for y in range(10):
                if g[(x, y)] > 9:
                    g[(x, y)] = 0
                    numFlashes += 1

                    # This x, y octopus is flashing, so increment its non-zero neighbors:
                    for xOffset, yOffset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        if x+xOffset != -1 and y+yOffset != -1 and x+xOffset != 10 and y+yOffset != 10:
                            if g[(x+xOffset, y+yOffset)] != 0:
                                g[(x+xOffset, y+yOffset)] += 1
                                if g[(x+xOffset, y+yOffset)] > 9:
                                    atLeastOneNeighborFlashed = True
        if not atLeastOneNeighborFlashed:
            break
    return numFlashes


#displayGrid(grid)
i = 0
while True:
    nextStepGrid(grid)

    inSync = True
    for x in range(10):
        for y in range(10):
            if grid[(x, y)] != 0:
                inSync = False
                break

    #displayGrid(grid)
    i += 1
    if inSync: break

print(i)