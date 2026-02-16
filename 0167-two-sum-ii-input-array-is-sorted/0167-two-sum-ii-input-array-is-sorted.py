class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1 indexed array and sorted in non decreasing order 
        # [2,7,11,15] -> target = 9. Thereforwe output [1, 2]
        pointerOne = 0
        pointerTwo = len(numbers)  - 1
        while pointerOne < pointerTwo:
            addition = numbers[pointerOne] + numbers[pointerTwo]
            if addition < target:
                pointerOne = pointerOne +  1
            elif addition > target: 
                pointerTwo = pointerTwo - 1
            elif addition == target:
                return [pointerOne +1, pointerTwo + 1]
                
            #else return the two indicies in a list
