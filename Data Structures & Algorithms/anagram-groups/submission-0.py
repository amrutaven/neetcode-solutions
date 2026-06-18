class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {} #key is the sorted str, value is a vector of unsorted strings
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in str_dict:
                str_dict[sorted_str] = []
            
            str_dict[sorted_str].append(str)
        
        return list(str_dict.values())



        