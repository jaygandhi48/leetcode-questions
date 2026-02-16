class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Make an arr with n+1 buckets 
        citationsLen = len(citations)
        bucketsLen = citationsLen + 1
        buckets = [0] * (bucketsLen)
        for i in citations:
            if i >= citationsLen: 
                #Place this in the last buckets. Just write 1 there
                buckets[citationsLen] += 1
            else:
                buckets[i]+=1
    
        count = 0
        for j in range(citationsLen, -1, -1): #loop from backwards
            count += buckets[j]
            if count >= j:          
                return j
        
           





