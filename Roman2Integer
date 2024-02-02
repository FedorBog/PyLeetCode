class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        r2i_convert = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000,
                       }

        str_length = len(s)

        for ind, romanSymb in enumerate(s):

            if ind == str_length - 1:
                result += r2i_convert[romanSymb]
                break

            currI = r2i_convert[romanSymb]
            nextI = r2i_convert[s[ind+1]]

            if currI < nextI:
                result -= currI
            else:
                result += currI

        return result


print(Solution.romanToInt('LVIII'))
