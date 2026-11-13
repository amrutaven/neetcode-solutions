class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #put them into the hash maps that have the key as the chars in order

        dict = {}

        for s in strs:
            #since sorted returns a list of ordered characters
            key = "".join(sorted(s))
            if key not in dict:
                dict[key] = []
            
            dict[key].append(s)

        
        return list(dict.values())
        

        