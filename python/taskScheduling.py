def leastInterval(tasks, n) -> int:
    counter = {}
    for t in tasks:
        if not t in counter:
            counter[t] = 0
        counter[t] += 1
    row = sorted([(k, v) for k, v in counter.items()], key = lambda x: -x[1])

    #now I have a sorted task row. Perfect
    cycles = 0
    while row:
        newRow = []
        #print(row, cycles)
        for i in range(n + 1):
            if i < len(row):
                el, ct = row[i]
                #print(el)
                if ct > 1:
                    newRow.append((el, ct - 1))
                cycles += 1
            elif newRow:
                #print('wait')
                cycles += 1 # do nothing
            else:
                return cycles
        j = 0
        idx = j + n + 1
        while idx < len(row):
            if row[0][1] < row[idx][1]:
                el, ct = row[idx]
                if ct > 1:
                    newRow.append((el, ct - 1))
                cycles += 1
            else:
                newRow.extend(row[idx:])
                idx += len(row)
                #break # break out of this while loop
            idx += 1
        row = newRow
    return cycles

print(leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))