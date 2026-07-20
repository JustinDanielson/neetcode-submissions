class Solution:    
    def encode(self, strs: List[str]) -> str:
        def _encode_str(s:str) -> str:
            return ",".join([str(len(s)), s])

        header = str(len(strs)) # ex: 2
        body = ",".join(map(_encode_str, strs)) # ex: 5,Hello,5,World

        return header + "," + body

    def decode(self, s: str) -> List[str]:
        res = list()
        l_ptr = s.find(",")
        total_items = int(s[:l_ptr])
        
        l_ptr += 1
        for i in range(total_items):
            # the strlen may be 1 digit or multiple digits, so we need to find the next comma
            delim_loc = s.find(",", l_ptr)
            strlen = int(s[l_ptr: delim_loc])
            l_ptr = delim_loc + 1 #advance pointer
            next_str = s[l_ptr: l_ptr + strlen]
            l_ptr = l_ptr + strlen + 1 #advance pointer
            res.append(next_str)
        return res