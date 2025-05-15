
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (size_t i = 1; i < nums.size(); ++i) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};

int main() {
    int n;
    cin >> n;                       // read number of elements
    vector<int> x(n);
    for (int i = 0; i < n; ++i)     // read the elements
        cin >> x[i];

    Solution sol;
    vector<int> result = sol.runningSum(x);

    for (int v : result)            // print the running sum
        cout << v << ' ';
    cout << '\n';

    return 0;
}
