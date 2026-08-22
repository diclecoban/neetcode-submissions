class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = str()
        for string in strs:
            encoded_string = encoded_string + str(len(string)) + '#' + string

        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i
            while(s[j] != '#'):
                j = j + 1

            length = int(s[i:j])
            beginWord = j + 1
            endWord = beginWord + length
            word = str(s[beginWord:endWord])
            decoded_strs.append(word)
            i = endWord

        return decoded_strs