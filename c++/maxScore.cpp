class Solution {
public:
    int maxScore(string s) {
        // we can just compute the max of all possible scores for O(N)
        // every possible solution is O(N)
        int zeroLeft = 0;
        int oneRight = 0;
        int maxS = 0;
        for (char c : s) {
            if (c == '1') {
                oneRight++;
            }
        }
        // left, right must always exist, so don't consider case where all in one
        for (int i = 0 ; i < s.size() - 1; i++) {
            if (s[i] == '1') {
                oneRight--;
            } else {
                zeroLeft++;
            }
            maxS = max(maxS, oneRight + zeroLeft);
        }
        return maxS;
    }
};

int main() {
    string s;
    cin >> s;
    Solution sol;
    cout << sol.maxScore(s) << endl;