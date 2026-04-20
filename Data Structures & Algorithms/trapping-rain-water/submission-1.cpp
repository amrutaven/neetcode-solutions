class Solution {
public:
    int trap(vector<int>& height) {
        //two pointer approach
        int left = 0;
        int right = height.size() - 1;
        int maxRight = 0;
        int maxLeft = 0;
        int water = 0;

        while (left < right) {
            if (height[left] <= height[right]) {
                //now we consider the left max
                maxLeft = max(height[left], maxLeft);
                water += maxLeft - height[left]; //minimum is 0
                left++;
            }
            else {
                maxRight = max(height[right], maxRight);
                water += maxRight - height[right];
                right--;
            }
        }
        return water;
        
    }
};