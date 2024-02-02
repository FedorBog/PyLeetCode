class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]        
        """
        result = list()

        mem_num_indx = dict()
        for indx, num in enumerate(nums):
            missNum = target - num
            memIndx = mem_num_indx.get(missNum)
            if memIndx != None:
                result.append(memIndx)
                result.append(indx)
                return result
            else:
                mem_num_indx[num] = indx


print(Solution.twoSum([3, 3], 6))
