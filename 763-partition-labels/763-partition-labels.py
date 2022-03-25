class Solution:
    # time complexity - o(n) and space - o(26) so constant it says only small letters
    def partitionLabels(self, s: str) -> List[int]:
        items = {}
        dict_={}
        limit = 0
        size = 0
        solution = []
        rang = 0
        for i, c in enumerate(s):
            dict_[c] = i
        ''' s = "ababcbaca | defegde | hijhklij" '''
        limit = dict_[s[0]] 
        for i, c in enumerate(s): # i - index, c - element
            if i == limit:
                solution.append(abs(rang - (i+ 1)))
                rang = i + 1
                if i + 1 < len(s): 
                    limit = dict_[s[i+1]]
            if dict_[c] > limit:
                limit = dict_[c]
        return solution