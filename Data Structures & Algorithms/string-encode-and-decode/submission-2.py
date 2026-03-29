class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += i + "SPLIT"
        return output

    def decode(self, s: str) -> List[str]:
        print(s)
        x = s.split("SPLIT")
        return x[:-1]