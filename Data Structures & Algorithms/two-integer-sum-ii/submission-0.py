class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        taille = len(numbers)
        for i in range(taille - 1):
            first = numbers[i]
            for j in range(i+1, taille):
                second = numbers[j]
                somme = first + second
                if somme > target:
                    break
                elif somme == target:
                    return [i + 1, j + 1]
        