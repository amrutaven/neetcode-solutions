class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        book = {}
        for num in nums:
            book[num] = book.get(num, 0) + 1
        
        reverse_book = sorted(book.items(), key=lambda item: item[1], reverse = True)

        return [num for num, freq in reverse_book[:k]]


        