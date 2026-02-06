class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = (k*(k+1)) //2
        for i in sorted(set(nums)): 
            if i <= k: 
                ans = ans - i
                k = k + 1
                ans = ans + k

        return ans
    
