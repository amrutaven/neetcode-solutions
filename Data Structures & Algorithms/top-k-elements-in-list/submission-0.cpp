class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //hash table first -- works
        unordered_map<int, int> first_map;
        for (int num : nums) {
            first_map[num]++;
        }

        //now push it into a priority queue as pairs
        priority_queue<pair<int, int>, vector<pair<int, int>>, CompareSecond> pq;

        //now turn all the entries in the hash map into pairs and put them into the pq
        for (auto it : first_map) {
            pq.push({it.first, it.second});
        }
        
        //now push them into the vector
        vector<int> output;
        for (int i = 0; i < k; i++) {
            output.push_back(pq.top().first);
            pq.pop();
        }
        return output;
        
    }

    struct CompareSecond {
        bool operator()(const pair<int, int>&lhs, const pair<int, int>&rhs) {
            return lhs.second < rhs.second;
        }

    };
};
