class Solution(object):
    def canVisitAllRooms(self, rooms):
        stack = [0]
        visited = set([0])

        while stack:
            node = stack.pop()
            for key in rooms[node]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
            if len(visited) == len(rooms):
                return True
        return False

        #T:O(V+E), S:O(V)