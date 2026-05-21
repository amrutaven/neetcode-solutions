class Solution {
public:
    bool isPalindrome(string s) {
        //remove spaces
        string s_temp = "";
        for (char ch : s) {
            if (isalnum(ch)) {
                s_temp += tolower(ch);
            }
        }
        for (int i = 0; i < s_temp.size() / 2; i++) {
            if (s_temp[i] != s_temp[s_temp.size() - 1 - i]) {
                return false;
            }
        }

        return true;
    }
};
