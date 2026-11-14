class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #key: number and value: frequency
        book = {}

        for num in nums:
            book[num] = book.get(num, 0) + 1
        
        return sorted(book, key=book.get, reverse=True)[:k]



