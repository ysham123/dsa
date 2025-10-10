class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        visited = [0] * numCourses
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        #time O(V + E), Space: O(V+E)