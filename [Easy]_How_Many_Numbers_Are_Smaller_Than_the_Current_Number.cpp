class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> num = nums;
        sort(num.begin(), num.end()); // Sort the vector

        unordered_map<int, int>
            dictionary; // Dictionary to store element and its index

        for (int i = 0; i < num.size(); i++) {
            if (dictionary.find(num[i]) == dictionary.end()) {
                dictionary[num[i]] = i; // Store the first occurrence of the
                                        // element with its index
            }
        }

        vector<int> ans;
        for (int j = 0; j < nums.size(); j++) {
            ans.push_back(dictionary[nums[j]]); // Map original element to its
                                                // index in sorted array
        }

        return ans;
    }
};