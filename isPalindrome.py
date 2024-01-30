def isPalindrome(x: int) -> bool:
    num = x
    reversed_num = 0

    while num != 0 and num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return True if reversed_num == x else False


class Solution:
    pass


print(isPalindrome(-0))
