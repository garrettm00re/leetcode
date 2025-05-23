#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        char mapTo[128] = {};   // s[i] → t[i]
        char mapFrom[128] = {}; // t[i] → s[i]

        for (int i = 0; i < s.size(); ++i) {
            char sI = s[i], tI = t[i];

            if (mapTo[sI] && mapTo[sI] != tI) return false;
            if (mapFrom[tI] && mapFrom[tI] != sI) return false;

            mapTo[sI] = tI;
            mapFrom[tI] = sI;
        }
        return true;
    }
};

int main() {
    Solution sol;
    cout << "Enter s: " << endl;
    string s;
    cin >> s;
    cout << "Enter t: " << endl;
    string t;
    cin >> t;
    cout << sol.isIsomorphic(s, t) << endl;
    return 0;
}
