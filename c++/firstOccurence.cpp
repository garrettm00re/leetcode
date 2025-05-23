#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int N = needle.size(), H = haystack.size(); // fine cuz size_t nonzero
        if (H < N) return -1;
        for (int i = 0; i < H - N + 1; i++) {
            if (needle == haystack.substr(i, N)) return i;
        }
        return -1;
    }
};

int main() {
    Solution sol;
    cout << "Enter haystack: " << endl;
    string haystack;
    cin >> haystack;
    cout << "Enter needle: " << endl;
    string needle;
    cin >> needle;
    cout << sol.strStr(haystack, needle) << endl;
    return 0;
}