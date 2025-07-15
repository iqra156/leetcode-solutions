class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        int finishTime = 0;
        double totalWaitTime = 0;
        for (int i = 0; i < customers.size(); i++) {
            int arriveTime = customers[i][0];
            int cookTime = customers[i][1];
            if (finishTime < arriveTime) {
                finishTime = arriveTime;
            }
            finishTime += cookTime;
            totalWaitTime += finishTime - arriveTime;
        }
        return totalWaitTime / customers.size();
    }
};