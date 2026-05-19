class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "<EMPTY>"
        return "<$JOIN_TOK$>".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "<EMPTY>":
            return []
        return s.split("<$JOIN_TOK$>")
