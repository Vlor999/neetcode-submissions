class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            for group in groups:
                if "".join(sorted(group[0])) == sorted_word:
                    group.append(word)
                    break
            else:
                groups.append([word])
        return groups