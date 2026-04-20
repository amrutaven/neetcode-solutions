class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int> > output;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; //this skips this iteration
            }

            int start = i + 1;
            int end = nums.size() - 1;

            while (start < end) {
                sum = nums[i] + nums[start] + nums[end];
                if (sum == 0) {
                    output.push_back({nums[i], nums[start], nums[end]});
                    start++;
                    end--;

                    while (start < end && nums[end] == nums[end + 1]) {
                        end--;
                    }
                    while (start < end && nums[start] == nums[start - 1]) {
                        start++;
                    }
                }
                else if (sum > 0) {
                    end--;
                }
                else {
                    start++;
                }
            }

        }
        return output;
        
    }
};
