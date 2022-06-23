class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.fixed = k
        self.head = self.tail = None
        self.h = True

    def enQueue(self, value: int) -> bool:
        if self.isEmpty(): # first enqueue
            self.head = self.tail = 0
            self.q[0] = value
            return True
        if self.isFull(): #full
            return False
        if (self.tail+1) == self.fixed: #not first enqueue
            self.tail = 0
        else:
            self.tail+=1
        self.q[self.tail] = value
        if self.h == True:self.h=False
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head] = None
        if self.head == self.tail:
            self.head = self.tail = None
            self.h = True
        elif (self.head+1) == self.fixed:
            self.head = 0
        else:
            self.head+=1
        return True

    def Front(self) -> int: 
        if self.isEmpty():return -1
        return self.q[self.head] 
        
    def Rear(self) -> int:
        if self.isEmpty():return -1
        return self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.head == None 

    def isFull(self) -> bool:
        if self.head == None:return False
        return (self.head + self.fixed - 1) % self.fixed == self.tail
