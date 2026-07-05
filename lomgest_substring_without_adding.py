class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(sol.lengthOfLongestSubstring("bbbbb"))  # 1
    print(sol.lengthOfLongestSubstring("pwwkew"))  # 3