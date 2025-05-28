#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> counter;
        for (int num : arr) {
            counter[num]++;
        }
        unordered_set<int> counts;
        for (const auto& [key, value] : counter) {
            bool isUnique = counts.insert(value).second;
            if (!isUnique) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution solution;
    vector<int> arr;
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }
    string result = solution.uniqueOccurrences(arr) ? "UNIQUE" : "NON-UNIQUE";
    cout << "Each element in your array has a " << result << " number of occurences." << endl;
}