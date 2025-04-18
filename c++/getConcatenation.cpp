#include <vector>
#include <iostream>

using namespace std;
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int length = nums.size();
        for (int i = 0; i < length; i++) {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<int> result = solution.getConcatenation(nums);
    cout << "Result: ";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}