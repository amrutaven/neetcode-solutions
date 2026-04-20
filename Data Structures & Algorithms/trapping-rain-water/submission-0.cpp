class Solution {
public:
    int trap(vector<int>& height) {
        //first we need to build the left and right subarrays
        vector<int> left(height.size());
        vector<int> right(height.size());

        //build left array
        int maxLeft = 0;
        for (int i = 0; i < height.size(); i++) {
            left[i] = max(height[i], maxLeft);
            if (maxLeft < height[i]) maxLeft = height[i];
        }

        //build right array
        int maxRight = 0;
        for (int i = height.size() - 1; i >= 0; i--) {
            right[i] = max(height[i], maxRight);
            if (maxRight < height[i]) maxRight = height[i];
        }

        int totalWater = 0;
        for (int i = 0; i < height.size(); i++) {
            totalWater += min(right[i], left[i]) - height[i];
        }
        return totalWater;
        
    }
};