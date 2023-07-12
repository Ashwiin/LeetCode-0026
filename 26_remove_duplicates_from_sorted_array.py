class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes the duplicates from the given sorted array `nums` in-place.
        Returns the number of unique elements in `nums`.
        
        :type nums: List[int]
        :rtype: int
        """
        
        # Use set to get unique elements and sort the result in ascending order
        nums[:] = sorted(set(nums))
        
        return len(nums)
