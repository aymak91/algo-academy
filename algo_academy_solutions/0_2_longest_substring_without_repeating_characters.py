# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        char_set = set()
        
        while right < len(s):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            max_length = max(max_length, right-left+1)
            char_set.add(s[right])
            right += 1
        
        return max_length