class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int pt1 = 0;
        int pt2 = numbers.size() - 1;
        while (pt1 != pt2) {
            if (numbers[pt1] + numbers[pt2] > target) {
                pt2--;
            }
            else if (numbers[pt1] + numbers[pt2] < target) {
                pt1++;
            }
            else {
                cout << pt1 << " " << pt2;
                return {pt1 + 1, pt2 + 1};
            }
        }
        return {};
    }
};
