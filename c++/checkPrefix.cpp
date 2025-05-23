#include <string_view>
#include <iostream>

using namespace std;

class Solution {
public:
    bool checkPrefix(string_view sv, string searchWord) {
        for (int i = 0; i < searchWord.size(); i++) {
            if (searchWord[i] != sv[i]){
                return false;
            }
        }
        return true;
    }

    int isPrefixOfWord(string sentence, string searchWord) {
        int start = 0;
        int end = 0; // inclusive
        int wordIndex = 1;
        string_view sv(sentence);
        for (int i = 0; i < sentence.size(); i++) {
            while (sv[i] == ' ') {
                i++;
            }
            start = i;
            end = i;
            while (i < sentence.size() && sv[i] != ' ') {
                i++;
                end++;
            }
            bool isPrefix = checkPrefix(sv.substr(start, end), searchWord);
            if (isPrefix) {
                return wordIndex;
            } else {
                wordIndex++;
            }
        }
        return -1;        
    }
};

int main() {
    Solution sol;
    cout << sol.isPrefixOfWord("i love eating burger", "burg") << endl;
    return 0;
}