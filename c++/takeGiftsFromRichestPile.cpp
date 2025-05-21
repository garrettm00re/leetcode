#include <vector>
#include <queue>
#include <cmath>

using namespace std;

class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> pq(gifts.begin(), gifts.end());

        while (k-- > 0 && pq.top() > 1) { 
            int maxGift = pq.top();
            pq.pop();
            pq.push(static_cast<int>(sqrt(maxGift)));
        }

        long long total = 0;
        while (!pq.empty()) {
            total += pq.top();
            pq.pop();
        }

        return total;
    }
};

int main() {
    Solution sol;
    vector<int> gifts = {25, 64, 9, 4, 100};
    int k = 4;
    cout << sol.pickGifts(gifts, k) << endl;
    return 0;
}
