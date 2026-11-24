class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #parse through strs, order str and put into dict if it does not exist
        #put the unordered version in the list which is the value

        book = {}

        for s in strs:
            if "".join(sorted(s)) not in book:
                book["".join(sorted(s))] = []
            
            book["".join(sorted(s))].append(s)
        
        return list(book.values())
        

        

        
        

        