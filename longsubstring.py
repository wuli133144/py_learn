"""

输入: "abcabcbb"
输出: 3
解释: 无重复字符的最长子串是 "abc"，其长度为 3。

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) ==0:
            return None
        length=len(s)
        Max=1
        Maxpace=1
        L=[]
        for i in range(length):
            j=i+1
            L.append(s[i])
            while j < length:
                  if L.count(s[j]) == 0:
                      L.append(s[j])
                      Maxpace+=1

                  else:
                      L=[]
                      if Max < Maxpace:
                          Max=Maxpace

                      Maxpace=0
                  j+=1

        return Max

    def lengthOfLongestSubstring2(self, s):
        """
        :param s:
        :return:
        """
        if len(s) == 0:
            return None
        size=len(s)
        iterm={}
        presize=0
        Maxsize=0

        for i in range(size):
            iterm[s[i]]=""
            presize+=1
            if len(iterm) != presize:
                 presize=len(iterm)
                 if Maxsize < presize:
                     Maxsize=presize
                     presize=0
            else:
                presize+=1
                pass
            i+=1


        return Maxsize






s=Solution()
ret=s.lengthOfLongestSubstring2("xaabvvxxxxxx")
print(ret)
