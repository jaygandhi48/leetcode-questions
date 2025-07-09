class Solution:
    def binarySearch(self, nums, target, direction):
        l, r = 0, len(nums) - 1
        directionIndex = -1
        while l <= r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else: 
                directionIndex = mid
                if not direction: 
                    r = mid - 1
                else:
                    l = mid + 1
        return directionIndex
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowest = self.binarySearch(nums, target, False)
        highest = self.binarySearch(nums, target, True)
        return [lowest, highest]
        #nums is sorted in increasing order 

        #Function for lowerbound. 

        #Since its sorted then you can just keep going until you reach the last repeating value. 

        #for example after lower bound is found get the index and go from there?
    


    


        