class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        int n = nums.size(); // Get the size of the input vector

        std::vector<int> ans(n); // Initialize the answer vector with size 'n'

        // Loop through each index in 'nums'
        for (int i = 0; i < n; ++i) {
            ans[i] = nums[nums[i]]; // Assign the value as per the problem's
                                    // requirement
        }

        return ans; // Return the result vector
    }
};