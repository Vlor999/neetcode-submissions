class Solution:
    def merge(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return sorted(nums1 + nums2)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        tailleTot = len(nums1) + len(nums2)
        if tailleTot % 2 == 0:
            indices = (tailleTot // 2 - 1, tailleTot // 2)
        else:
            indices = (tailleTot // 2, tailleTot // 2)
        mergedList = self.merge(nums1, nums2)
        return (mergedList[indices[0]] + mergedList[indices[1]]) / 2