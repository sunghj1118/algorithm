class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for st in strs[1:]:
            # reduce prefix until it matches
            while not st.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix