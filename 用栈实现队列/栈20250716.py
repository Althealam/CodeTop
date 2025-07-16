class MyQueue:

    def __init__(self):
        # in负责push，out负责pop
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x: int) -> None:
        """将元素x推到队列的末尾"""
        self.stack_in.append(x)
        
    def pop(self) -> int:
        """从队列的开头移除并返回元素"""
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        
    def peek(self) -> int:
        """返回队列开头的元素"""
        ans = self.pop() 
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        if len(self.stack_in)==0 and len(self.stack_out)==0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()