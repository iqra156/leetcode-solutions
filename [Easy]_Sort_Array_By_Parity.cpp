class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int left = 0; // Pointer for even numbers
        // Use a 'for' loop to iterate over the array
        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] % 2 == 0) { // Check if the element is even
                // Swap the even number to the left side
                swap(nums[left], nums[right]);
                left++; // Move the 'left' pointer forward
            }
        }
        return nums; // Return the array sorted by parity
    }
};
//  we can use for and while loop both works same.it initialize pointer variable
//  ,right move for loop and swap with left if there is even on it.Then left
//  will move one index forward after swapping.When right complete the condition
//  of for loop nums is returned.