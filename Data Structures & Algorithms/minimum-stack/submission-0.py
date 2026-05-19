class MinStack:

    def __init__(self):
        self.mins = []
        self.vals = []
        

    def push(self, val: int) -> None:
        if len(self.mins) == 0:
            self.mins.append(val)
        elif self.mins[-1] > val:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])
        self.vals.append(val)
            

    def pop(self) -> None:
        self.mins.pop()
        self.vals.pop()
        

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
