def getStartOfMarkers(value):
    startOfPacket = -1 
    startOfMessage = -1 
    for i in range(len(value) - 3):
        char = set()
        for j in range(i, i + 4):
            char.add(value[j])
        if (len(char) == 4):
            startOfPacket = i + 4
            break
    for i in range(len(value) - 13):
        char = set()
        for j in range(i, i + 14):
            char.add(value[j])
        if (len(char) == 14):
            startOfMessage = i + 14
            break
    return startOfPacket, startOfMessage

# with open('data.txt') as file:
#     for line in file:
#         print(getStartOfMarkers(line))

