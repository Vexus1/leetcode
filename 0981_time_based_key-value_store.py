class TimeMap:
    def __init__(self):
        self.time_map: dict[str, list[str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map.keys():
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.time_map.get(key, [])
        left = 0
        right = len(values)-1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1))
print(timeMap.get("foo", 3))
print(timeMap.set("foo", "bar2", 4))
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
