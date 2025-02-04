class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      # Create an empty dictionary to count stones  
      count = {}    
      aux = 0
      # Count the occurrences of each stone
      for letter in stones:
         count[letter] = count.get(letter, 0) + 1
      # Check how many jewels are in our stones
      for jewel in jewels:
         aux += count.get(jewel, 0)
      return aux