class MedianFinder:

    def __init__(self):
        self.small,self.large = [],[]

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0]+self.large[0])/2.0

        """
        Heap
            Min Heap
            Max Heap
        Insert -> log n 
            min -> O(1)
        
        Max heap -> O(1) max


    maintain two heaps
    mineheap ->  second half of the array
    maxheap -> first of array

    [1,2,3,4,5,6,7,8,9,1]
    second half - min heap = 5,6,7,8,9,10
    first half = max heap = 1,2,3,4


    1,2,3 -> max heap
    5,6,7 -> min heap

    1,2,3,4
    5,6,7
    8
    1,2,3,4
    5,6,7,8
    1,2,3,4,5
     7,8,9,10

    Batch Mode -> table -> sort -> result -> median
    Sttream Mode -> constantly coming through the pip / network

    
heapify

Insert -> 2

        addNum
            

        """
        
        