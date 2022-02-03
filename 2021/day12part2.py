#data = 'start-A,start-b,A-c,A-b,b-d,A-end,b-end'.split(',')
#data = 'dc-end,HN-start,start-kj,dc-start,dc-HN,LN-dc,HN-end,kj-sa,kj-HN,kj-dc'.split(',')
data = 'DA-xn,KD-ut,gx-ll,dj-PW,xn-dj,ll-ut,xn-gx,dg-ak,DA-start,ut-gx,YM-ll,dj-DA,ll-xn,dj-YM,start-PW,dj-start,PW-gx,YM-gx,xn-ak,PW-ak,xn-PW,YM-end,end-ll,ak-end,ak-DA'.split(',')

# Create the cave network data structure:
caveNetwork = {} # key is a caves, value is a list of destination caves
for connection in data:
    src, dst = connection.split('-')
    caveNetwork.setdefault(src, [])
    caveNetwork[src].append(dst)

    caveNetwork.setdefault(dst, [])
    caveNetwork[dst].append(src)

#print(caveNetwork)


def visit(cave, visitedOnce, twiceCave, totalPaths, currentPath):
    currentPath.append(cave)

    if cave == 'end':
        #print(','.join(currentPath))
        currentPath.pop()
        return totalPaths + 1  # BASE CASE

    if cave.islower() and cave not in visitedOnce:
        visitedOnce.add(cave)
    elif cave.islower() and cave in visitedOnce:
        assert twiceCave == ''
        twiceCave = cave

    for dst in caveNetwork[cave]:
        if dst == 'start':
            continue  # skip the start cave, it's not a valid destination

        if dst in visitedOnce and twiceCave != '':
            continue # skip this, because we already have visited it once and we already have a twice cave.

        totalPaths = visit(dst, visitedOnce, twiceCave, totalPaths, currentPath) # RECURSIVE CASE

    if twiceCave == cave:
        twiceCave = ''  # Unset twiceCave
    elif cave.islower() and cave in visitedOnce:
        visitedOnce.remove(cave)

    currentPath.pop()
    return totalPaths




print(visit('start', set(), '', 0, []))

