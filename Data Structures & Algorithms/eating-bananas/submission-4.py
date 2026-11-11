class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)



        #binary search on the piles
        while (right > left):
            middle = (right + left) // 2
            total = 0
            for num in piles:
                total += math.ceil(num / middle)
            if total <= h:
                right = middle
            
            else:
                left = middle + 1

        
        return right

            
        
            

