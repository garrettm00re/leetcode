from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def topological_sort_dfs(graph):
            def dfs(v, visited, stack, callStack):
                visited.add(v)
                callStack.add(v)
                for neighbor in graph[v]:
                    if neighbor in callStack:
                        cycle[0] = True
                        break
                    if not cycle[0] and neighbor not in visited:
                        dfs(neighbor, visited, stack, callStack)
                stack.append(v)
                callStack.remove(v)
            
            visited = set()
            stack = []
            callStack = set() # represents all nodes on the path (being traveled by) to the current node
            cycle = [False]

            for idx, node in enumerate(graph):
                if not cycle[0] and idx not in visited:
                    dfs(idx, visited, stack, callStack)
            return stack[::-1] if not cycle[0] else [] # Reverse the stack to get the topological order
        
        graph = [[] for _ in range(numCourses)]
        for post, pre in prerequisites:
            graph[pre].append(post)
        
        return topological_sort_dfs(graph)