def getFullOverlapCount(filename):
    count = 0
    with open(filename) as file:
        for line in file:
            first, second = line.strip().split(",")
            lfirst, rfirst = first.split("-")
            lsecond, rsecond = second.split("-")
            if int(lfirst) <= int(lsecond) and int(rfirst) >= int(rsecond): 
                count += 1
            elif int(lsecond) <= int(lfirst) and  int(rsecond) >= int(rfirst):
                count += 1
    return count

def getOverlapCount(filename):
    count = 0
    with open(filename) as file:
        data = [i for i in file.read().strip().split("\n")]
    for entry in data:
        first, second = entry.split(",")
        first = [int(i) for i in first.split("-")]
        second = [int(i) for i in second.split("-")]
        if first[0] in range(second[0], second[1] + 1) or first[1] in range(second[0], second[1] + 1):
            count += 1
        elif second[0] in range(first[0], first[1] + 1) or second[1] in range(first[0], first[1] + 1):
            count += 1
    return count

#print(getFullOverlapCount("data.txt"))
#print(getOverlapCount("data.txt"))