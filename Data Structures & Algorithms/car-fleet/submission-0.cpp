class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {

        vector<pair<int, int> > pos_speed;
        for (int i = 0; i < position.size(); i++) {
            pos_speed.push_back({position[i], speed[i]});
        }
        sort(pos_speed.begin(), pos_speed.end(),[](const auto& a, const auto& b) {
                 return a.first > b.first;
                });

        stack<double> times;
        for (int i = 0; i < pos_speed.size(); i++) {
            double time = double(target - pos_speed[i].first) / pos_speed[i].second;
            if (times.empty() || time > times.top()) {
                times.push(time);
            }
        }
        return times.size();

    }
};