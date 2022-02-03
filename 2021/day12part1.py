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



def visit(cave, alreadyVisitedSmallCaves, totalPaths):
    if cave == 'end':
        return totalPaths + 1  # BASE CASE

    if cave.islower():
        alreadyVisitedSmallCaves.add(cave)

    for dst in caveNetwork[cave]:
        if dst not in alreadyVisitedSmallCaves:
            totalPaths = visit(dst, alreadyVisitedSmallCaves, totalPaths) # RECURSIVE CASE

    if cave.islower():
        alreadyVisitedSmallCaves.remove(cave)
    return totalPaths




print(visit('start', set(), 0))

