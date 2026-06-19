class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = {}
        for num in nums:
            book[num] = book.get(num, 0) + 1
        
        heap = []
        for num, freq in book.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
            



        