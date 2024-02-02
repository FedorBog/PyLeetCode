class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        result = ''
        indx = 0
        do_next = True

        while do_next:
            curr_char = ''
            for word in strs:

                if indx == len(word):
                    do_next = False
                    break

                if not curr_char:
                    curr_char = strs[0][indx]

                if curr_char != word[indx]:
                    do_next = False
                    break

            indx += 1

            if do_next == True:
                result += curr_char

        return result


print(Solution().longestCommonPrefix(['flower', 'flow', 'flight']))
print(Solution().longestCommonPrefix(['flower', 'flow', '']))
print(Solution().longestCommonPrefix(['flower', 'flow', 'flow']))
print(Solution().longestCommonPrefix(['dog', 'racecar', 'car']))
print(Solution().longestCommonPrefix(['']))
