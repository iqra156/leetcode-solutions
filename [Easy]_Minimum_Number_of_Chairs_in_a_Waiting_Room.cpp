class Solution {
public:
    int minimumChairs(string s) {
        int person = 0;
        int chairs = 0;

        for (char i : s) {
            if (i == 'E') {
                person++;
                if (chairs < person) {
                    chairs++;
                }
            } else if (i == 'L') {
                person--;
            }
        }

        return chairs;
    }
};