class MyStack:

    def __init__(self):
        self.stack_list=[]
        self.stack_size=0

    def push(self, value):
        self.stack_size+=1
        self.stack_list.append(value)

    def is_empty(self):
        return self.stack_size==0


    def pop(self):
        if self.is_empty():
            return None
        self.stack_size-=1
        return self.stack_list.pop()

    def size(self):
        return self.stack_size

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

