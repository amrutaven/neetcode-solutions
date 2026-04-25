class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        //base cases
        if (heights.size() == 1) {
            return heights[0];
        }

        stack<int> indices;

        int running_max = 0;
        for (int i = 0; i < heights.size(); i++) {
            while (!indices.empty() && heights[i] < heights[indices.top()]) {
                int height = heights[indices.top()];
                indices.pop();
                
                int boundary = indices.empty()? -1 : indices.top();
                int width = i - boundary - 1;

                running_max = max(running_max, width * height);

            }
            indices.push(i);
        }

        //if everything increases
        int i = heights.size();
        while (!indices.empty()) {
            int height = heights[indices.top()];
            indices.pop();

            int boundary = indices.empty()? -1 : indices.top();
            int width = i - boundary - 1;

            running_max = max(running_max, width * height);
        }

        return running_max;
    }

};