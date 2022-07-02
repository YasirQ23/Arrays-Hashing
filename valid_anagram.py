#  1st Solution

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_ = {}
        for i in s:
            dict_[i] = dict_.get(i, 0) + 1
        for i in t:
            dict_[i] = dict_.get(i, 0) - 1
        for i in dict_.values():
            if i != 0:
                return False
        return True

# revised solution


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_ = {}
        for i in range(len(s)):
            dict_[s[i]] = dict_.get(s[i], 0) + 1
            dict_[t[i]] = dict_.get(t[i], 0) - 1
        for i in dict_:
            if dict_[i] != 0:
                return False
        return True

# their solution


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
