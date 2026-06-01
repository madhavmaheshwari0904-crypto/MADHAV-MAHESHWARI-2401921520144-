class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        list_=[0]*1001
        for n,from_,to in trips:
            list_[from_]+=n
            list_[to]-=n
        for i in list_:
            capacity-=i
            if(capacity<0):
                return False
        return True            