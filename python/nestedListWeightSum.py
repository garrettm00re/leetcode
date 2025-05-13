class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested, depth):
            if nested.isInteger():
                nonlocal total
                total += depth * nested.getInteger()
            for item in nested.getList():
                dfs(item, depth + 1)
                    
        total = 0
        for topLevelItem in nestedList:
            dfs(topLevelItem, 1)
        return total