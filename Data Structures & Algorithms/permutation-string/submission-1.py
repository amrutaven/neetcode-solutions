class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict_s1 = {}
        dict_s2 = {}

        for c in s1:
            dict_s1[c] = dict_s1.get(c, 0) + 1
        
        for i in range(len(s1)):
            c = s2[i]
            dict_s2[c] = dict_s2.get(c, 0) + 1

        num_windows = len(s2) - len(s1) + 1

        for i in range(num_windows):

            if dict_s2 == dict_s1:
                return True
                
            if i == num_windows - 1:
                break

            dict_s2[s2[i]] -= 1
            if dict_s2[s2[i]] == 0:
                del dict_s2[s2[i]]
            
            c = s2[i + len(s1)]
            
            dict_s2[c] = dict_s2.get(c, 0) + 1
        
        return False


            
                    

        
        
        