class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        i = 0
        while i < len(self.requests):
            if self.requests[0] < t-3000:
                self.requests.pop(0)
            else:
                break
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)