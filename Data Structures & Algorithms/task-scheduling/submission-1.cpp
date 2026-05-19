#include <vector>
#include <functional>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

class Solution {
    public:
        int leastInterval(vector<char>& tasks, int n) {
            map<char, int> counter;
            for (char task : tasks) {
                counter[task]++;
            }

            priority_queue<int> maxHeap;
            for (auto& entry : counter) {
                maxHeap.push(entry.second);
            }

            int time = 0;
            queue<pair<int, int>> cooldown;

            while (!maxHeap.empty() || !cooldown.empty()) {
                time++;

                if (!maxHeap.empty()) {
                    int freq = maxHeap.top() - 1;
                    maxHeap.pop();
                    if (freq > 0) {
                        cooldown.push({freq, time + n});
                    }
                }

                if (!cooldown.empty() && cooldown.front().second == time) {
                    maxHeap.push(cooldown.front().first);
                    cooldown.pop();
                }
            }

            return time;
        }
    };