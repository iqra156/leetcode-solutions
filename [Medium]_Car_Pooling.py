class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_distance = 1001
        diff = [0] * max_distance

        for num_passengers, start, end in trips:
            diff[start] += num_passengers
            diff[end] -= num_passengers

        current_passengers = 0
        for change in diff:
            current_passengers += change
            if current_passengers > capacity:
                return False
        return True
