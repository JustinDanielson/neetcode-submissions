class Solution:
    # Previous Implementation: 4,4,2,1,4,this,is,a,test
    # Current Implementation: 4,4,this,2,is,1,a,4,test
    # Previous implementation lets you process the metadata, for example finding the longest string
    # Current implementation allows you to encode/decode on the fly without maintaining the lengths 
    #    of all the strings or pre-processing the header
    # Previous implementation could do on the fly, 
    #    but you could need to maintain a pointer to the current str length, 
    #    and a pointer to where the actual strings start. This means preprocessing all the str lengths
    #    which could be slow if data is massive
    def encode(self, strs: List[str]) -> str:
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