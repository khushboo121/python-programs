#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution:
   def longestCommonPrefix(self, strs: List[str]) -> str:
     
     res = ""

     for i in range(0,len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
     return res

if __name__ == "__main__":

    strs = ["flower","flow","flight"]
    object1 = Solution()
    print(object1.longestCommonPrefix(strs))        

  