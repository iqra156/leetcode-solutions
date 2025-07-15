class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n  # initialize the array with zeros

        for first, last, seats in bookings:
            ans[first - 1] += seats  # Add seats at the start index
            if last < n:
                ans[last] -= seats  # Subtract seats after the end index

        for i in range(1, n):
            ans[i] += ans[i - 1]  # Prefix sum to apply the difference

        return ans
