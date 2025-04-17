#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers are not palindromes (see edge cases)
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }

        // For even length: x == reversedHalf
        // For odd length: x == reversedHalf / 10 (middle digit can be ignored)
        return x == reversedHalf || x == reversedHalf / 10;
    }
};

int main() {
    Solution solution;
    int x = 123;
    bool result = solution.isPalindrome(x);
    cout << "Is " << x << " a palindrome? " << (result ? "Yes" : "No") << endl;
    return 0;
}