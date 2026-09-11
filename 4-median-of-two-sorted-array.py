class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        merged = nums1 + nums2
        merged.sort()

        if len(merged) % 2 ==0:
            median = (merged[len(merged)// 2-1] + merged[len(merged)//2])/2

        else:
            median = (merged[len(merged)//2])

        return median


        

