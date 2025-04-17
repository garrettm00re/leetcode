def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    visited = set([0])
    keys = rooms[0]
    n = len(rooms)
    while keys and len(visited) < n:
        curr = keys.pop()
        if not curr in visited:
            visited.add(curr)
            keys.extend(rooms[curr])
    return len(visited) == n