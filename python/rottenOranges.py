def orangesRotting(grid: list[list[int]]) -> int:
    newRot, rotted, healthy = set(), set(), set()
    minutes = 0
    adjacent = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                healthy.add((row, col))
            elif grid[row][col] == 2:
                newRot.add((row, col))
                rotted.add((row, col))
    totalOranges = len(healthy) + len(rotted)
    while len(rotted) != totalOranges and len(newRot):
        newNewRot = set()
        for row, col in newRot:
            for dr, dc in adjacent:
                nR, nC = row + dr, col + dc
                if (nR, nC) in healthy:
                    healthy.remove((nR, nC))
                    newNewRot.add((nR, nC))
                    rotted.add((nR, nC))
        newRot = newNewRot
        minutes += 1
    return -1 if len(rotted) != totalOranges else minutes
