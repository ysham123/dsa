class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set()
        provinces = 0
        n = len(isConnected)

        for i in range(n):
            if i not in visited:
                stack = [i]
                visited.add(i)
                while stack:
                    node = stack.pop()
                    for neighbor in range(n):
                        if isConnected[node][neighbor] == 1 and neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
    
                provinces +=1
        return provinces

        #T:O(n^2), S:O(n)