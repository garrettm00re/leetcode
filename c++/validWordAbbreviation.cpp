#include <string>
#include <iostream>

using namespace std;


class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        // get the number
        // discern between "wildcard" and hardcoded character in abbr
        int abbrI = 0, wordI = 0;
        while (abbrI < abbr.size()) {
            char c = abbr[abbrI];
            int abbreviationLength = 0;
            while (abbrI < abbr.size() && isdigit(c)) {
                if (c == '0' && abbreviationLength == 0) return false;
                abbreviationLength = (abbreviationLength * 10) + (c - '0');
                abbrI++;
                c = abbr[abbrI];
            }
            if (abbreviationLength) {
                wordI += abbreviationLength;
            } else if (c != word[wordI]) {
                return false;
            } else {
                abbrI++;
                wordI++;
            }
        }
        return wordI == word.size();
    }
};

int main() {
    Solution solution;
    string word, abbr;
    cin >> word >> abbr;
    cout << solution.validWordAbbreviation(word, abbr) << endl;
}
