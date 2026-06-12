class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans=defaultdict(list)
        #print(ans)
        for i in strs:
            s=''.join(sorted(i))
            ans[s].append(i)
            #print(s)
            #print(ans)
        return list(ans.values())    