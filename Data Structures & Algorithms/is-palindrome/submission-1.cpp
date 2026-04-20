class Solution {
public:
    bool isPalindrome(string s) {
        string s_mod = "";
        for (char c : s) {
            if (isalnum(c)) {
                c = tolower(c);
                s_mod += c;
            }
        }
        cout << s_mod;
        s = s_mod;

        for (int i = 0; i < s.length() / 2; i++) {
            if (s[i] != s[s.length() - i - 1]) {
                return false;
            }
        }
        return true;
        
    }
};
