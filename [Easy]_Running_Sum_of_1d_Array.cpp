class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int temp = 0;
    std:
        vector<int> array;
        for (int i : nums) {
            temp = temp + i;
            array.push_back(temp);
        }
        return array;
    }
};