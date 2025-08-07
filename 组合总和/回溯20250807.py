class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self.traversal(candidates, target, res, path, 0)
        return res
    
    def traversal(self, candidates, target, res, path, startIndex):
        if sum(path)==target:
            res.append(path[:])
            return 
        if sum(path)>target:
            return
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.traversal(candidates, target, res, path, i)
            path.pop()
