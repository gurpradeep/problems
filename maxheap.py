class MaxHeap:

    def __init__(self):
        self.heap=[]


    

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)
    
    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap)>1:
            max = self.heap[0]
            self.heap[0]=self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max
        elif len(self.heap)==1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None



    def __percolateUp(self, index)
        parent = (index-1)//2
        if index <=0:
            return 
        if self.heap[parent]<self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index]= tmp
            self.__percolateUp(self, parent)


    def __maxHeapify(self,index)