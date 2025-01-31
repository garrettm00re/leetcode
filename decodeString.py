#https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def decodeString(self, s: str) -> str:
        def handleBracketContents(idx):
            # returns a decoded string, closeBracket idx for one open close bracket pair
            # idx corresponds to the index after the open bracket
            string = ""
            while idx < len(s):

                char = s[idx]
                try:
                    # get the numerical multiplier
                    num = int(char)
                    idx += 1
                    while not s[idx] == '[':
                        num *= 10
                        num += int(s[idx])
                        idx += 1
                    
                    substring, idx = handleBracketContents(idx + 1) # idx now == to the one right after the close bracket
                    string += num * substring
                except Exception as e:
                    if char == ']':
                        return string, idx + 1
                    else:
                        string += char
                        idx += 1
            return string, idx
        string, finalIdx = handleBracketContents(0)
        return string

                    
                
