class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        if (nums.size() == 1) {
            return 1;
        }

        unordered_set<int> values;
        int lowest = nums[0];
        int highest = nums[0];
        for (int num : nums) {
            values.insert(num);
            if (num < lowest) {
                lowest = num;
            }
            if (num > highest) {
                highest = num;
            }
        }

        int max = 0;
        int count = 0;
        for (int i = lowest; i <= highest; i++) {
            if (values.count(i)) {
                count++;
                if (max < count) {
                    max = count;
                }
                
            }
            else {
                count = 0;
            }

        }
        return max;
        
    }
};
