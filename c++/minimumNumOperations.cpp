#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> seen;
        int N = nums.size();
        int i = N - 1;

        // Find where uniqueness breaks when traversing from the end
        while (i >= 0 && seen.insert(nums[i]).second) {
            --i;
        }

        int removeCount = i + 1;
        return (removeCount + 2) / 3;  // same as ceil(removeCount / 3.0) but faster
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    cout << sol.minimumOperations(nums) << endl;
    return 0;
}