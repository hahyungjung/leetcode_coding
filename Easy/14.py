14.py

"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

"""

def longestCommonPrefix(strs: List[str]) -> str:

        ans = ""
        
        if len(strs) == 0: return ans

        for i in range(len(min(strs, key = len))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                ans += c
            else:
                break
                
        return ans


