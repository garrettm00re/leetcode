#https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/

def minSwaps(data: list[int]) -> int:
    windowSize = 0
    sofar = []
    for num in data:
        windowSize += num
        sofar.append(windowSize)
    numInWindow, bestWindowIndex = sofar[windowSize - 1], 0
    maxNumInWindow = numInWindow
    del sofar
    
    if windowSize == len(data):
        return 0 #nowhere to move any ones
    for i in range(1, len(data) - windowSize + 1):
        numInWindow -= data[i - 1]
        numInWindow += data[i + windowSize - 1]

        if numInWindow > maxNumInWindow:
            bestWindowIndex = i
            maxNumInWindow = numInWindow
    return windowSize - maxNumInWindow
