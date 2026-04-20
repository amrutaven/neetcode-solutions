//find the minimum value, secure the index location
//starting from the minimum value location, index through and find the max value
//return max minus min

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int running_min = prices[0];
        int max_profit = 0;
        vector<int> values;
        for (int i = 1; i < prices.size(); i++) {
            running_min = min(running_min, prices[i]);
            max_profit = max(prices[i] - running_min, max_profit);
        }
        return max_profit;
    }
};