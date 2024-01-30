def romanToInt(s: str) -> int:
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    exception_romans = {'I': ['V', 'X'],
                        'X': ['L', 'C'],
                        'C': ['D', 'M']}

    int_result = 0
    for x, letter in enumerate(s):
        if letter not in exception_romans:
            int_result += roman_to_int[letter]
        elif letter in exception_romans and x+1 != len(s):
            if s[x+1] in exception_romans[letter]:
                int_result -= roman_to_int[letter]
            else:
                int_result += roman_to_int[letter]
        else:
            int_result += roman_to_int[letter]

    return int_result


class Solution:
    pass
