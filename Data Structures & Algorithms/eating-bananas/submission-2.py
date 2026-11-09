class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        middle = (right + left) // 2


        #binary search on the piles
        while (right > left):
            total = 0
            for num in piles:
                total += math.ceil(num / middle)
            if total <= h:
                right = middle
            
            else:
                left = middle + 1

            middle = (right + left) // 2
        
        return middle

            
        
            

