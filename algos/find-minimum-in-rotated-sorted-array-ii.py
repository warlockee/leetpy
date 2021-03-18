"""
If you have not see the [explaination](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/356286/Best-Python-Solution-(How-to-Solve-all-Similar-Problem-Explained)) of the previous [question](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), please see it first.
This problem has duplicate value in compare to the previous.
The difference is that when you cut the rotated array into half, there might not be a sorted array occur.
You might have something like `[2,2,2,2,1,2,2,2,2,2,2]`.
If we can't find either left-half or right-half is sorted, we simply reduce the range (`l = l+1, r = r-1`) and use the same method again.
"""
class Solution(object):
    def findMin(self, nums):
        if nums is None or len(nums)==0:
            return None
        m = nums[0]
        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2
            m = min(m, nums[l], nums[p], nums[r])

            if nums[l]<nums[r]:
                break
            elif nums[l]<nums[p]:
                l = p+1
            elif nums[p]<nums[r]:
                r = p-1
            else:
                l = l+1
                r = r-1
        return m
