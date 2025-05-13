#https://neetcode.io/problems/jump-game-ii
def jump(nums: list[int]) -> int:
    def startJump(idx):
        j = nums[idx]
        numJumps = float("inf") if idx != len(nums) - 1 else -1 # return value
        for landingIdx in range(idx + 1, min(j + idx + 1, len(nums))):
            if not landingIdx in idxToJumpNum:
                idxToJumpNum[landingIdx] = startJump(landingIdx)
            numJumps = min(idxToJumpNum[landingIdx], numJumps)
        return numJumps + 1
    idxToJumpNum = {} # maps idxs to min num jumps
    return startJump(0)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        nums = [int(num) for num in sys.argv[1:]]
        for n in nums:
            assert isinstance(n, int)
        print(jump(nums))