import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return the kth largest element in the list given that  1 < k <= 10^5. 
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k: #Keep only k elements
                heapq.heappop(min_heap) # Remove smallest

        return min_heap[0]
        



            
            
