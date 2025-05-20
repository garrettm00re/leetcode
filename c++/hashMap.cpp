#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class MyHashMap {
public:
        int numBuckets = 1;
        float loadFactor = 64;
        int numEl = 0;
        vector<vector<pair<int, int>>> buckets = vector<vector<pair<int, int>>>(numBuckets); // store
        int resizeFactor = 64;
        // is the maximum possible hash value of note? --> no as we use modulo to determine bucketIdx
    MyHashMap() {
    }
    
    void put(int key, int value) {
        if ((float) (numEl + 1) / (numBuckets) >= loadFactor) {
            resize();
        }
        numEl++;
        int bucketIdx = hashKey(key);
        pair<int, int> p = {key, value};
        for (auto& p : buckets[bucketIdx]) {
            if (p.first == key) {
                p.second = value;
                return;
            }
        }
        buckets[bucketIdx].push_back(p);        
    }
    
    int get(int key) {
        int bucketIdx = hashKey(key);
        for (const auto& p : buckets[bucketIdx]) {
            if (p.first == key) {
                return p.second;
            }
        }
        return -1; // key not found
    }
    
    void remove(int key) {
        int bucketIdx = hashKey(key);
        vector<pair<int, int>>& bucket = buckets[bucketIdx];
        for (int i = 0; i < bucket.size(); i++) {
            if (bucket[i].first == key) {
                bucket.erase(bucket.begin() + i);
                break;
            }
        }
    }
private:
    void resize() {
        // we only grow the map in this implementation
        int newNumBuckets = numBuckets * resizeFactor;//nextPrime(numBuckets);
        vector<vector<pair<int, int>>> newBuckets(newNumBuckets);
        for (const auto& bucket : buckets) {
            for (const auto& p : bucket) {
                int newBucket = p.first & (newNumBuckets - 1);
                newBuckets[newBucket].push_back(p);
            }
        }
        numBuckets = newNumBuckets;
        buckets = newBuckets;

    }

    int hashKey(int key) {
        return key & (numBuckets - 1);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */