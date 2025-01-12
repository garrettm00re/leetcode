def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    # brute force implementation is the best I can think of for the time being
    def RLE(string):
        last = ""
        i = 0
        ct = 0
        res = ""
        while i < len(string):
            if ct > 0 and string[i] != last:
                res += str(ct) + last
                last, ct = "", 0
            if ct == 0:
                last = string[i]
            if string[i] == last:
                ct += 1
            i += 1
        res += str(ct) + last
        return res
    i = 1
    lastRLE = "1"
    while i < n:
        lastRLE = RLE(lastRLE)
        i += 1
    return lastRLE