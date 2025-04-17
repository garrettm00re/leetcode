# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# see also: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/6208791/simple-intuitive-python-solution-beats-100/
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == "":
        return []

    numChars = {
    '2': ['a', 'b', 'c'], 
    "3" : ['d', 'e', 'f'], 
    "4" : ['g', 'h', 'i'],
    "5" : ['j', 'k', 'l'], 
    "6" : ['m', 'n', 'o'], 
    "7": ['p', 'q', 'r', 's'], 
    "8" : ['t', 'u', 'v'], 
    "9" : ['w', 'x', 'y', 'z']
    }
    combos = [""]
    
    for dig in digits:
        newCombos = []
        for combo in combos:
            for char in numChars[dig]:
                newCombos.append(combo + char)
        combos = newCombos
    return combos