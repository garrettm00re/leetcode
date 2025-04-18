#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        unordered_map<char, char> closeOpen = {
            {')', '('}, {']', '['}, {'}', '{'}
        };

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push_back(c);
            } else {
                if (stack.empty() || stack.back() != closeOpen[c]) {
                    return false;
                }
                stack.pop_back();
            }
        }
        return stack.empty();
    }
};

int main() {
    Solution solution;
    string s = "[[{{{((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))}}}]]";
    bool result = solution.isValid(s);
    cout << result << endl;
}

