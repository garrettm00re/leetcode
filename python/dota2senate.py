#https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75


# UGLY SOLUTION --> functional and efficient, but ripe for beautification
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rCount = len([1 for i in senate if i == 'R'])
        dCount = len(senate) - rCount
        rBans, dBans = 0, 0 # rBans is number of r curr banned, dBans is symm.
        if not (rCount and dCount):
            return "Radiant" if rCount else "Dire"
        while True:
            newSenate = ""
            
            for senator in senate:
                if senator == 'R':
                    if rBans:
                        rBans -= 1
                    else:
                        dBans += 1
                        dCount -= 1
                        newSenate += senator
                        
                elif senator == 'D':
                    if dBans:
                        dBans -= 1
                    else:
                        rBans += 1
                        rCount -= 1
                        newSenate += senator
                        
                if not (rCount and dCount):
                    return "Radiant" if rCount else "Dire"

                
            senate = newSenate
        
                

        