class Solution:
    # TODO: change encoding
    # Current: 4,4,2,1,4,this,is,a,test
    # Desired: 4,4,this,2,is,1,a,4,test
    def encode(self, strs: List[str]) -> str:
        # 4,
        # 4,2,1,4,
        # this,is,a,test
        def _encode_str(s:str) -> str:
            return str(len(s)) + "," + s
        total_items = len(strs)
        if total_items == 0:
            return "0,"
        header = f"{len(strs)},"
        return header + ",".join(map(_encode_str, strs))

    def decode(self, s: str) -> List[str]:
        l_ptr = s.find(",")
        total_items = int(s[:l_ptr])
        if total_items == 0:
            return []
        
        strs = list()
        l_ptr += 1
        for i in range(total_items):
            delim_loc = s.find(",", l_ptr)
            strlen = int(s[l_ptr: delim_loc])
            l_ptr = delim_loc + 1
            next_str = s[l_ptr: l_ptr + strlen]
            l_ptr = l_ptr + strlen + 1
            strs.append(next_str)
        return strs