#include <cstdio>
#include <string>
#include <cstdlib>

using namespace std;  // Option 1: Makes all std items available

class Solution {
public:
    int scoreOfString(string s) {
        int totalScore = 0;
        int last = 0;
        for (char c : s) {
            // need to skip first iter or splice s
            if (last == 0) {
                printf("%d\n", last);
                last = int(c);
                printf("%d\n", last);
            } else {
                totalScore += abs(int(c) - last);
                last = int(c);
            }
        }
        return totalScore;
    }
};

// Add this main function:
int main() {
    Solution solution;
    string test = "abcd";  // test string
    int result = solution.scoreOfString(test);
    printf("Score for %s: %d\n", test.c_str(), result);
    return 0;
}