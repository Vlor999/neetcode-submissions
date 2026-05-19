class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        elements = [(key, value) for key, value in counter.items()]
        elements.sort(key=lambda x : x[1], reverse=True)
        elements = elements[:k]
        return [elem[0] for elem in elements]
