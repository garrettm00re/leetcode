class Solution {
public:
    unordered_map<char, int> getCounter() {
        return {{'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}};
    }

    void printCounter(unordered_map<char, int> counter) {
         for (const auto& pair : counter) {
            cout << pair.first << ":" << pair.second << " ";
        }
        cout << endl;
    }

    int countVowelSubstrings(string word) {
        // brute
        unordered_map<char, int> counter = getCounter();
        int count = 0;
        int localCount = 0;
        for (int i = 0; i < word.size(); i++) {
            localCount = 0;
            printCounter(counter);
            for (int j = i; j < word.size(); j++) {
                if (counter.find(word[j]) != counter.end()) {
                    counter[word[j]]++;
                    if (counter['a'] > 0 && counter['e'] > 0 && counter['i'] > 0 && counter['o'] > 0 && counter['u'] > 0) {
                        localCount++;
                    }
                } else if (localCount > 0) { 
                        count += localCount;
                        counter[word[i]]--;
                        break;
                } else {
                    i = j + 1;
                    counter = getCounter();
                    printCounter(counter);
                    break;
                }
            }
        }
        return count;
    }
};