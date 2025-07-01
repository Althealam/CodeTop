# 时间复杂度：O(mn)，m和n分别是输入矩阵的行数和列数
# 空间复杂度：O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1
        while left<=right and top<=bottom:
            for j in range(left, right+1): # 1-2-3
                ans.append(matrix[top][j])
            for i in range(top+1, bottom+1): # 6-9
                ans.append(matrix[i][right])
            if left<right and top<bottom:
                for j in range(right-1, left, -1): # 8
                    ans.append(matrix[bottom][j])
                for i in range(bottom, top, -1): # 7-4
                    ans.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        return ans