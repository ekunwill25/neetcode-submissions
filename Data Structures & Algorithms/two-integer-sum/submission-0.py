class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums): # sets an index to a value
            diff = target - n # creating a variable for the difference between target and current n
            if diff in prevMap: # looking for difference inside the hashmap
                return [prevMap[diff], i] # returns if the difference is inside the hashmap
            prevMap[n] = i # updating the hashmap
        return

        