#include <iostream>
#include <climits>

using namespace std;

class Solution {
public:
    int addDigits(int num) {
        int newNum;
        while (num > 9) {
            newNum = 0;
            while (num > 0) {
                newNum += num % 10;
                num /= 10; // should round down due to int type
            }
            num = newNum;
        }
        return num;
    }
};

int main() {
    cout << "Enter a number <= 2^31 - 1: ";
    long long y;
    cin >> y;
    if (y > INT_MAX) {
        cout << "Number is too large" << endl;
        return 1;
    }
    int x = static_cast<int>(y);
    Solution sol;
    cout << sol.addDigits(x) << endl;
    return 0;
}