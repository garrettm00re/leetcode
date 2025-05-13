def rotate(self, matrix: List[List[int]]) -> None:
    N = len(matrix)
    numAxial = N//2 # the number of "rings" in a matrix that need to be traversed
    for i in range(numAxial):
        origin = (-1 - i, i) # the starting poing of ringwise iteration
        stripSize = N - (2 * i) - 1 # the number of full curr -> next loops that need to be completed for the given ring
        for stripIndexer in range(stripSize):
            start = (origin[0] - stripIndexer, origin[1])
            curr = start
            currItem = matrix[curr[0]][curr[1]]
            while True:
                r, c = curr[1], -1 - curr[0] # next indices
                nextItem = matrix[r][c] # old value in next slot
                matrix[r][c] = currItem # overwrite old value with current item
                curr = (r, c)
                currItem = nextItem # now that currItem has been inserted, adjust the value of currItem to align with the new r, c
                if curr == start: # we have completed the loop
                    break
