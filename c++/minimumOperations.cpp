#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int seen[101];
        int positive = 0;
        for (int num : nums) {
            if (num > 0 && !seen[num]) {
                positive++;
                seen[num]++;
            }
        }
        return positive;
    }
};

int main() {
    Solution solution;
    vector<int> nums;
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        nums.push_back(num);
    }
    cout << solution.minimumOperations(nums) << endl;
    return 0;
}
