class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> map;
        map.insert({'{', '}'});
        map.insert({'(', ')'});
        map.insert({'[', ']'});

        unordered_set<char> opens;
        opens.insert('{');
        opens.insert('[');
        opens.insert('(');

        stack<char> values;
        for (char c : s) {
            if (opens.count(c)) {
                values.push(c);
            }
            else {
                if (!values.empty() && map[values.top()] == c) {
                    values.pop();
                }
                else {
                    return false;
                }
            }
        }
        return values.empty();
        
    }
};