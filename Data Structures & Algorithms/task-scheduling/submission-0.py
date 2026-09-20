import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        time=0
        while heap:
            temp=[]
            slots=n+1
            while slots>0 and heap:
                freq=-heapq.heappop(heap)

                freq-=1
                if freq>0:
                    temp.append(freq)
                time+=1
                slots-=1

            for freq in temp:
                heapq.heappush(heap,-freq)

            if heap:
                time+=slots
        return time
