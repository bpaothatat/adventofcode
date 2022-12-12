import re
import copy

def getCargoTop(filename):
    with open(filename) as file:
        stacks, instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))
        instructions = [re.findall(r'\d+', instruction) for instruction in instructions]
        instructions = [list(map(int, i)) for i in instructions]
        bucket_size = int(max(stacks[-1].split(" ")))
        buckets = [[] for i in range(bucket_size)]
        for i in reversed(range(len(stacks) - 1)):
            for j in range(1, bucket_size + 1):
                value = stacks[i][stacks[-1].index(str(j))]
                if value != ' ':
                    buckets[j - 1].append(value)
        second_buckets = copy.deepcopy(buckets)

        for instruction in instructions:
            items = []
            for i in range(instruction[0]):
                value = buckets[instruction[1] - 1].pop()
                buckets[instruction[2] - 1].append(value)
                second_value = second_buckets[instruction[1] -1].pop()
                items.append(second_value)
            items.reverse()
            second_buckets[instruction[2] -1] = second_buckets[instruction[2] -1] + items
        return ''.join([bucket[-1] for bucket in buckets]), ''.join([bucket[-1] for bucket in second_buckets])
#print(getCargoTop('data.txt'))