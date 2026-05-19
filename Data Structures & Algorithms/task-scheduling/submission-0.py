import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        taskCounts = Counter(tasks)
        maxHeap = [-freq for freq in taskCounts.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()

        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq < 0:
                    cooldown.append((freq, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time
