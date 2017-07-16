"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median_index = []
        if (len(nums1) + len(nums2)) % 2:
            median_index = [(len(nums1) + len(nums2)) // 2]
        else:
            median_index = [(len(nums1) + len(nums2)) // 2, ((len(nums1) + len(nums2)) // 2) - 1]

        i, j = 0, 0

        median = []
        curr = -1
        for k in range(len(nums1 + nums2)):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    curr = nums1[i]
                    i += 1
                else:
                    curr = nums2[j]
                    j += 1
            elif i < len(nums1):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            if k in median_index:
                median.append(curr)
        return sum(median) / len(median)

print(Solution().findMedianSortedArrays([1], [3, 4]))
