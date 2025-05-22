class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int queryIndex = 0;
        priority_queue<int> available; 
        priority_queue<int, vector<int>, greater<>> running; 

        
        sort(queries.begin(), queries.end());

        for (int i = 0; i < nums.size(); ++i) {
            
            while (queryIndex < queries.size() && queries[queryIndex][0] <= i) {
                available.push(queries[queryIndex][1]);
                ++queryIndex;
            }

            
            while (!running.empty() && running.top() < i) {
                running.pop();
            }

            
            while (running.size() < nums[i]) {
                if (available.empty()) return -1;
                if (available.top() < i) return -1;

                running.push(available.top());
                available.pop();
            }
        }

        return available.size();
    }
};
