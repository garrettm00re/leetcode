# https://neetcode.io/problems/jump-game
def canJump(self, nums) -> bool:
    visited = set() # shouldnt matter that I don't have 0 in it
    indexes = set([0])
    while indexes:
        newIndexes = set()
        for i in range(len(indexes)):
            curr = indexes.pop()
            if not curr == len(nums) - 1:
                val = nums[curr]
                for add in range(val):
                    newIdx = curr + add + 1 # range lowers by one
                    if not newIdx in visited:
                        newIndexes.add(newIdx)
                        visited.add(newIdx)
            else:
                return True
        indexes = newIndexes
    return False
