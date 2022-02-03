class Solution:
    def __init__(self):
        self.i = 0

    def decodeString(self, s: str) -> str:
        result = ""
        while self.i < len(s) and s[self.i] != "]":
            if not s[self.i].isdigit():
                result += s[self.i]
                self.i += 1
            else:
                k = 0

                while self.i < len(s) and s[self.i].isdigit():
                    k = k * 10 + int(s[self.i])
                    self.i += 1
                print(result)
                self.i += 1
                decoded_string = self.decodeString(s)
                self.i += 1
                result += decoded_string * k
        return result