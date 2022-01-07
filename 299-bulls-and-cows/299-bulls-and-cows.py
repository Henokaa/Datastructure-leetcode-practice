class Solution(object):
    def getHint(self, secret, guess):
      
        bulls=set()
        for i,j in enumerate(guess):
            if j==secret[i]:
                bulls.add(i)
        counts={}
        for i,j in enumerate(secret):
            if i not in bulls:
                counts[j]=counts.get(j,0)+1
        b=0
        for i,j in enumerate(guess):
            if i not in bulls and counts.get(j,0):
                b+=1
                counts[j]-=1
        return '%dA%dB'%(len(bulls),b)