# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

# pretty fast, (beats 91%) and very simple

def minFlips(a: int, b: int, c: int) -> int:
    a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
    mLen = len(max((a, b, c), key = len))
    a = '0' * (mLen - len(a)) + a
    b = '0' * (mLen - len(b)) + b
    c = '0' * (mLen - len(c)) + c
    total = 0
    for idx in range(len(c)):
        if c[idx] == '1':
            total += 1 if a[idx] == b[idx] == '0' else 0
        if c[idx] == '0':
            if a[idx] == '1':
                total += 1
            if b[idx] == '1':
                total += 1
    return total