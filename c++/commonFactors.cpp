#include <iostream>

using namespace std;

class Solution {
public:
    int commonFactors(int a, int b) {
        int mini = min(a, b);
        int iter = 1;
        int totalCommon = 0;
        while (iter <= mini) {
            if (a % iter == 0 && b % iter == 0) {
                totalCommon++;
            }
            iter++;
        }
        return totalCommon;
    }
};

// linker looks for main function
int main() {
    Solution solution;
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    int result = solution.commonFactors(a, b);
    cout << "Result: " << result << '\n';
    return 0;
}