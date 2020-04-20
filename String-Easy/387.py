class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        # create a hashtable with letter: number of occurences structure
        for index, letter in enumerate(s):
            counter[letter] = 1 if not counter.get(letter) \
                else counter[letter] + 1

        for index, letter in enumerate(s):
            if counter[letter] == 1:
                return index

        return -1
