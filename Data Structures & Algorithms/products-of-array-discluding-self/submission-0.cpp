class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left(nums.size(), 1);
        vector<int> right(nums.size(), 1);

        //populate the left array
        for (int n = 1; n < nums.size(); n++) {
            left[n] = left[n - 1] * nums[n - 1];
        }

        //populate the right array
        //start at nums.size() - 2 because n - 1 is the last value
        for (int n = nums.size() - 2; n >= 0; n--) {
            right[n] = right[n + 1] * nums[n + 1];
        }
        
        for (int n = 0; n < nums.size(); n++) {
            cout << right[n] << " ";
            left[n] *= right[n];
        }

        return left;
 
    }
};
