class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        value = float("inf")
        while value != target:
            v = numbers[left] + numbers[right]
            if v == target:
                return [left + 1, right + 1]
            if v < target:
                left += 1
            else :
                right -= 1


        