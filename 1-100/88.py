class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p, q, k = m-1, n-1, m+n-1
        while p>=0 and q>=0:
            if nums1[p]<=nums2[q]:
                nums1[k] = nums2[q]
                k -= 1
                q -= 1
            else:
                nums1[k] = nums1[p]
                k -= 1
                p -= 1
        for i in range(q,-1,-1):
            nums1[k] = nums2[i]
            k -= 1
