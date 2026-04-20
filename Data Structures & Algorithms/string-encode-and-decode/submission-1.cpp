class Solution {
public:

    string encode(vector<string>& strs) {
        string send = "";
        for (int i = 0; i < strs.size(); i++) {
            send += "#" + to_string(strs[i].size()) + "#" + strs[i];
        }
        return send;
    }

    vector<string> decode(string s) {
        if (s == "") return {};
        int counter = 0;
        vector<string> output;
        while (counter < s.size()) {
            int curr_size = 0;
            if (s[counter] == '#') {
                counter++;
                string num = "";
                while (s[counter] != '#') {
                    num += s[counter];
                    counter++;
                }
                counter++; //skip the next #
                curr_size = stoi(num);
                output.push_back(s.substr(counter, curr_size));
                counter += curr_size;
            }
        }
        return output;

    }
};
