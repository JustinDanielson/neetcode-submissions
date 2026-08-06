from collections import defaultdict
class TimeMap:
    '''
    This class will store key,value pairs and preserve historical values by using timestamps.
    timeMap.set("alice", "happy", 1)
    timeMap.set("alice", "sad", 3)
    timeMap.get("alice", 1) -> happy
    timeMap.get("alice", 2) -> happy
    timeMap.get("alice", 3) -> sad
    Alice was happy from [1-2] and is sad from [3-INF]
    '''
    TS_IDX = 1
    VAL_IDX = 0
    def __init__(self):
        self.records: List[str, List[int,str]] = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps of set are strictly increasing.
        # Assuming that all future sets will have increasingly larger timestamp values
        self.records[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        loc = self._binary_search(key, timestamp)
        res = self.records[key][loc][TimeMap.VAL_IDX] if loc >= 0 else ""
        return res

    def _binary_search(self, key, timestamp) -> int:
        res = -1
        records = self.records[key]
        l, r = 0, len(records) - 1
        m = (l + r) // 2
        while l <= r:
            if records[m][TimeMap.TS_IDX] > timestamp:
                r = m - 1
            else: # records[m][TimeMap.TS_IDX] <= timestamp
                l = m + 1
                res = m
            m = (l + r) // 2
        
        return res