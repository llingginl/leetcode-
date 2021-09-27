from typing import List
import os
import sys


class Solution:
    def dsf(self, r, grid, visited):
        visited.append(r)
        for j in range(len(grid)):
            if grid[r][j] == 1 and j not in visited:
                visited[j]=1
                self.dsf(j, grid, visited)

    def findCircleNum(self, M) -> int:

        visited = []
        count = 0
        for row in range(len(M)):
            if row not in visited:
                self.dsf(row, M, visited)
                count += 1
        return count

x=input()
print(Solution().findCircleNum(x))