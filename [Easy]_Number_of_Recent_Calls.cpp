class RecentCounter {
public:
    RecentCounter() {}
    int ping(int t) {
        queue.push_back(t);
        int start = t - 3000;
        while (!queue.empty() && queue.front() < start) {
            queue.pop_front();
        }
        return queue.size();
    }
private:
    std::deque<int> queue;
};