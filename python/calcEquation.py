# class Solution:
#     def calcEquation(
#         self, equations: List[List[str]], values: List[float], queries: List[List[str]]
#     ) -> List[float]:
#         nodeEdge = {}  # char1 : (char2, char1/char2)

#         def addEdges(n1, n2, val):
#             for to, fro, value in [(n1, n2, val), (n2, n1, 1 / val)]:
#                 if not to in nodeEdge:
#                     nodeEdge[to] = []
#                 nodeEdge[to] = (fro, val)

#         for idx, (c1, c2) in enumerate(equations):
#             addEdge(c1, c2, values[i])
#             # nodeEdge[c1] = (c2, values[i])
#             # nodeEdge[c2] = (c1, 1/values[i])

#         remaining = set(nodeEdge.keys())
#         components = []  # (traversalOrder, cycleFound)
#         while remaining:
#             visited = set()
#             traversalOrder = []
#             stack = [
#                 c1
#             ]  # sort of hacky, but c1 will be mapped to a value. This way we don't have to handle extra logic
#             # enqueued = set([c1]) interesting idea, I wonder what adding to the stack/queue only if it's not already on it would do
#             cycleFound = None
#             while stack:
#                 curr = stack.pop()
#                 if not curr in visited:
#                     visited.add(curr)
#                     traversalOrder.append(
#                         curr
#                     )  # add only explored nodes so path is continuous
#                 for to, val in nodeEdge[curr]:
#                     if to in visited:
#                         cycleFound = to
#                     else:
#                         stack.append(adjacent[0])
#             remaining = remaining - visited
#             components.append(traversalOrder, cycleFound)
