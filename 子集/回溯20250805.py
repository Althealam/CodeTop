class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        path = []
        self.traversal(result, path, 0, nums)
        return result
    
    def traversal(self, result, path, startIndex, nums):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.traversal(result, path, i+1, nums)
            path.pop()

        