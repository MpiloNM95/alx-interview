#!/usr/bin/python3

from typing import List

def isWinner(x: int, nums: List[int]) -> str:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_count(n: int) -> int:
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    maria = 0
    ben = 0

    for num in nums:
        prime_count = get_prime_count(num)
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
