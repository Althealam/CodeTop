class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
        self.traversal(result, path, s, 0)
        return result
    
    def traversal(self, result, path, s, startIndex):
        if startIndex == len(s) and len(path)==4:
            result.append('.'.join(path[:]))
            return 
        for i in range(startIndex, len(s)):
            if self.isvalid(s[startIndex:i+1]):
                path.append(s[startIndex:i+1])
                self.traversal(result, path, s, i+1)
                path.pop()
    
    def isvalid(self, x):
        if int(x)<0 or int(x)>255:
            return False
        if int(x)!=0 and int(x[0])==0:
            return False
        if int(x)==0 and len(x)>1:
            return False
        return True
    


