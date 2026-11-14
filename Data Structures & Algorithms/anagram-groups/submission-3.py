class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #dict key: sorted string, value is a list of words with that anagram
        book = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in book:
                book[key] = []
            
            book[key].append(s)
        
        return list(book.values())
        

        
        

        