// Write your code here
#include <bits/stdc++.h>
using namespace std;

int search(vector<int>& nums) {
    if (nums.empty()) return -1;
    int l = 0, r = nums.size() - 1;
    while (l < r) {
        int mid = (l + r) / 2;
        if (nums[mid] > nums[r]) l = mid + 1;
        else r = mid;
    }
    return l;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int num;
        cin >> num;
        vector<int> nums(num);
        for (int i = 0; i < num; i++) cin >> nums[i];
        cout << search(nums) << endl;
    }
    return 0;
}
