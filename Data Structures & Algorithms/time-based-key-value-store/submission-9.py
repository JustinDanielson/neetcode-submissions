from collections import defaultdict
class TimeMap:
    '''
    This class will store key,value pairs and preserve historical values by using timestamps.
    ex: key -> value,ts
    '''
    VAL_IDX = 0
    TS_IDX = 1
    def __init__(self):
        self.records: List[str, List[int,str]] = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps of set are strictly increasing.
        self.records[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        loc = self._binary_search(key, timestamp)
        res = self.records[key][loc][TimeMap.VAL_IDX] if loc >= 0 else ""
        return res

    def _binary_search(self, key, timestamp) -> int:
        res = -1
        records = self.records[key]
        l, r = 0, len(records) - 1
        while l <= r:
            m = (l + r) // 2
            if records[m][TimeMap.TS_IDX] > timestamp:
                r = m - 1
            else: # records[m][TimeMap.TS_IDX] <= timestamp
                l = m + 1
                res = m
        return res