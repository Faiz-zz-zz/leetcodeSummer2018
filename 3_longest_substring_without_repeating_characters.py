"""

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        start, end = 0, 1
        max_len = 1
        letter_map = {s[start]: start}
        while end < len(s):
            if s[end] not in letter_map:
                letter_map[s[end]] = end
                end += 1
            else:
                new_start = letter_map[s[end]] + 1
                for i in range(start, new_start):
                    letter_map.pop(s[i])
                start = new_start
                letter_map[s[end]] = end
                end += 1
            max_len = max((max_len, end - start))
        return max_len
