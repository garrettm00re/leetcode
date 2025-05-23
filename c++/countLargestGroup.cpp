#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
Key optimizations:
-Use an array instead of a hashmap --> no resizing required as n <= 10^4 and the digit sum can't exceed 45
-Leverage the fact that nil values are already initialized to 0 (see * below)
*/
class Solution {
public:
    int countLargestGroup(int n) {
        int count[46] = {};  // digit sum can't exceed 45 (0 index is nothing)
        int maxGroupSize = 0;

        for (int i = 1; i <= n; ++i) {
            int sum = digitSum(i);
            int newCount = ++count[sum]; // *
            maxGroupSize = max(maxGroupSize, newCount);
        }

        int totalMaxGroups = 0;
        for (int i = 1; i <= 45; ++i) {
            if (count[i] == maxGroupSize) {
                ++totalMaxGroups;
            }
        }
        return totalMaxGroups;
    }

private:
    int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
};

int main() {
    int x;
    cin >> x;
    Solution sol;
    cout << sol.countLargestGroup(x) << endl;
    return 0;
}
