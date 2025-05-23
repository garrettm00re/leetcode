#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> constructRectangle(int area) {
        int sqrtArea = static_cast<int>(sqrt(area));
        for (int i = sqrtArea; i >= 1; --i) {
            if (area % i == 0) {
                return {area / i, i};
            }
        }
        return {};
    }
};

int main() {
    Solution sol;
    vector<int> result = sol.constructRectangle(4);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}