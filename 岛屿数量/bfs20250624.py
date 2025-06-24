# 时间复杂度：O(mxn) 每个节点最多被访问两次，第一次是在遍历网格时检查是否为未访问的陆地，另一次是在BFS中标记为已访问时
# 1. 遍历网格：O(mxn)
# 2. bfs
# 空间复杂度：O(mxn) visited数组用来标记每个单元格是否被访问过
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]
        self.res = 0
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and int(grid[i][j])==1:
                    self.res+=1
                    self.bfs(visited, grid, i, j)
        return self.res
    
    def bfs(self, visited, grid, x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y]=True

        while queue:
            x,  y =queue.popleft()
            for dx, dy in self.directions:
                next_x, next_y = x+dx, y+dy
                if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                    continue
                if int(grid[next_x][next_y])==1 and not visited[next_x][next_y]:
                    visited[next_x][next_y]=True
                    queue.append((next_x, next_y))
