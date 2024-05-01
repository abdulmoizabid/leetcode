from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        dict_s = Counter(s)
        dict_t = Counter(t)
        if(dict_s == dict_t):
                return True
        else:
            return False
            

if __name__ == "__main__":
    s = "rat"
    t = "car"
    obj = Solution()
    b = obj.isAnagram(s,t)
    print(b)
