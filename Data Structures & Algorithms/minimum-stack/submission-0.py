class MinStack:

    def __init__(self):
        self.stk = []
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stk:
            self.min_val = val
            self.stk.append(val - self.min_val) # 0
        else:
            self.stk.append(val - self.min_val)
            self.min_val = min(self.min_val, val)

        

    def pop(self) -> None:
        if not self.stk:
            return
        pop = self.stk.pop()
        if pop < 0:
            self.min_val = self.min_val - pop

        

    def top(self) -> int:
        top = self.stk[-1]
        if top > 0:
            return self.min_val + top
        else:
            return self.min_val
        

    def getMin(self) -> int:
        return self.min_val
        
