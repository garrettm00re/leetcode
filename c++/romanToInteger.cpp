#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        static unordered_map<char, int> map = {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };

        int total = 0;
        for (int i = 0; i < s.size(); ++i) {
            int curr = map[s[i]];
            int next = (i + 1 < s.size()) ? map[s[i + 1]] : 0;
            if (curr < next) {
                total += (next - curr);
                ++i;
            } else {
                total += curr;
            }
        }
        return total;
    }
};

int main() {
    Solution sol;
    string s;
    cout << "Enter a Roman numeral: ";
    cin >> s;
    cout << sol.romanToInt(s) << endl;
    return 0;
}
