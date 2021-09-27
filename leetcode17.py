import os
import sys
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:



        if not digits :return[]

        digit_map ={
            0 :"0",
            1: "1",
            2 :"abc",
            3 :"def",
            4 :"ghi",
            5 :"jkl",
            6 :"mno",
            7 :"pqrs",
            8 :"tuv",
            9 :"wxyz",
        }

        res = [""]

        for digit in digits:
            temp = []
            for ch in digit_map[int(digit)]:
                for str in res:
                    temp.append(str +ch)

            res =temp
            print(res)


        return res


x=input()
Solution().letterCombinations(x)
