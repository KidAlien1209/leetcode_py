class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nstr = str(n)
        i=0
        j=len(nstr)-1
        while i < j:
            if nstr[i] != nstr[j]:
                t=nstr[i]
                nstr[i]=nstr[j]
                nstr[j]=t
        return int(nstr)