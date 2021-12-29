class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        print(words)
        sortedwords = sorted(words, key = lambda x: x[-1])
        return " ".join(x[:-1] for x in sortedwords)