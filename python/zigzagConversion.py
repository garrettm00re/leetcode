def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    def nextPD(pos, direction):
        if numRows == 1:
            return 0, 0
        if direction == -1 and pos == 0:
            pos, direction = 1, 1
        elif direction == 1 and pos == numRows - 1:
            pos = 0 if numRows - 1 < 0 else numRows - 2
            direction = -1
        else:
            pos += direction
        return pos, direction

    pos = 0
    rows = ["" for _ in range(numRows)]
    direction = 1 # 1 or -1
    for idx in range(len(s)):
        rows[pos] += s[idx]
        pos, direction = nextPD(pos, direction)
    summed = ""
    for row in rows:
        summed += row
    return summed