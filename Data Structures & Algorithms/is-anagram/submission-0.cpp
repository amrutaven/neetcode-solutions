class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (char sh : s) {
            s_map[sh]++;
        }

        for (char th : t) {
            t_map[th]++;
        }
        
        return s_map == t_map;

    }
};