class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;
        int start = 0;
        int end = heights.size() - 1;

        while (start <= end) {
            //calculate the area with every iteration
            max_area = max(max_area, area(heights[start], heights[end], end - start));
            
            if (heights[start] < heights[end]) {
                start++;
            }
            else if (heights[start] > heights[end]) {
                end--;
            }
            else {
                start++;
                end--;
            }
            
        }
        return max_area;
        
    }

    int area (int height1, int height2, int width) {
        return min(height1, height2) * width;
    }
};
