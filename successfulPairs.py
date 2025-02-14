# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

# beats 94.66% in runtime and 96.83% in memory. I am actually getting pretty good at this.

def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    spellIdxs = sorted([i for i in range(len(spells))], key = lambda x : spells[x]) # counting sort = O(N)
    potions = sorted(potions, reverse = True)

    pairs = [0] * len(spells)
    potionIdx = 0
    for spellIdx in spellIdxs:
        spell = spells[spellIdx]
        while potionIdx < len(potions) and spell * potions[potionIdx] >= success:
            potionIdx += 1
        pairs[spellIdx] = potionIdx
    return pairs