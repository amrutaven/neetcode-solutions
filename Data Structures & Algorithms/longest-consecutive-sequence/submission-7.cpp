class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> values(nums.begin(), nums.end());
        int length = 0;
        int consec = 0;
        int possible_max = 0;

        for (int num : values) {
            if (!values.count(num - 1)) {
                length = 1;
                consec = num;

                //here we try to find the consecutive length
                while (values.count(consec + 1)) {
                    length++;
                    consec++;
                }
            }
            possible_max = max(possible_max, length);
        }
        return possible_max;
        
    }
};
