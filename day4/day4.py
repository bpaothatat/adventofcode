def getOverlapCount(filename):
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

print(getOverlapCount("data.txt"))
