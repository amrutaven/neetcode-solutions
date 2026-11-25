class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create hash map of the elements, order them in reverse, return the first k

        book = {}

        for num in nums:
            book[num] = book.get(num, 0) + 1
        
        return sorted(book, key=book.get, reverse=True)[:k]


