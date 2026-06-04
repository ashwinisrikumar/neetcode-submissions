class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time = time + 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time






        """
        X,X,Y,Y

        X Y _ X Y


        A A A B C

        A B C _ A _ _ _ A

        highest frquency count
        count = [
            'X': 2,
            Y': 2
        ]

        
        X, Y
        Y _ _ Y
        idle = Y = (count - 1) * gap = (2 - 1) * 2 = 2
        idle = Y = 
            fir this between the two Y's -> 2 - 1 = 1
            2 slots
            



        """
        