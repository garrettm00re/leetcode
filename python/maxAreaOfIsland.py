def maxAreaOfIsland(grid: list[list[int]]) -> int:
        explored = set()
        unexplored = set()
        queue = [(0,0)]
        land = grid[0][0] #True if land, False if water
        biggest, this = 0, 0
        directions = [(0, 1), (1,0), (-1, 0), (0, -1)]
        while queue:
          curr = queue.pop(0)
          if curr not in explored:
            print(curr, grid[curr[0]][curr[1]], land, this)
            explored.add(curr)
            unexplored.remove(curr) if curr in unexplored else None
            for d in directions:
              new = (curr[0] + d[0], curr[1] + d[1])
              if new not in explored and 0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0]):
                #print(new[0], len(grid), new[1], len(grid[0]))
                newIsLand = grid[new[0]][new[1]]
                unexplored.add(new)
                if newIsLand and land or (not newIsLand and not land):
                  queue.append(new)
            this += land
            if this > biggest:
                biggest = this
                this = 0
          if not queue:
            if unexplored:
              curr = unexplored.pop()
              queue = [curr]
              land = grid[curr[0]][curr[1]]
              
        print(len(explored), len(grid), len(grid[0]), len(unexplored))
        return biggest

def visualizeGrid(grid):
   for r in grid:
      print(r)

grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))
visualizeGrid(grid)