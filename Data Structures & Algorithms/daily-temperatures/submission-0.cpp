class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> values;
        vector<int> output(temperatures.size());

        values.push(temperatures.size() - 1);

        for (int i = temperatures.size() - 2; i >= 0; i--) {
            while (!values.empty() && temperatures[i] >= temperatures[values.top()]) {
                values.pop();
            } 
            if (!values.empty()) {
                output[i] = abs(i - values.top());
            }
            values.push(i);
        } 
        return output;
    }
};