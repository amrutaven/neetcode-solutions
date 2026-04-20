class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> values;

        unordered_set<string> operators;
        operators.insert({"+", "-", "*", "/"});

        for (string s : tokens) {
            if (!operators.count(s)) {
                values.push(stoi(s));
                continue;
            }

            int valTwo = values.top();
            values.pop();
            int valOne = values.top();
            values.pop();
            int toPush = 0;

            if (s == "+") {
                toPush = valOne + valTwo;
            }
            else if (s == "-") {
                toPush = valOne - valTwo;
            }
            else if (s == "*") {
                toPush = valOne * valTwo;
            }
            else {
                toPush = valOne / valTwo;
            }
            
            values.push(toPush);
        }
        return values.top();
        
    }
};