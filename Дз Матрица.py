from sys import stdin
from copy import deepcopy


class Matritsa:
    def __init__(self, lol):
        self.matritsa = deepcopy(lol)

    def add(self, other):
        other = Matritsa(other)
        res = []
        nums = []
        for i in range(len(self.matritsa)):
            for j in range(len(self.matritsa[0])):
                summa = other[i][j] + self.matritsa[i][j]
                nums.append(summa)
                if len(nums) == len(self.matritsa):
                    res.append(nums)
                    nums = []
        return Matritsa(res)

    def mul(self, other):
        if isinstance(other, int) or isinstance(other, float):
            res = [[other * x for x in y] for y in self.list2D]
            return Matritsa(res)
        elif self.dim_C != other.dim_R:
            return 'Нельзя'
        else:
            a = range(self.dim_C)
            b = range(self.dim_R)
            c = range(other.dim_C)
            res = []
            for i in b:
                res = []
                for j in c:
                    el, m = 0, 0
                    for k in a:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                res.append(res)
            return Matritsa(res)
    
    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matritsa)



