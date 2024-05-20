import os
import sys
class Mod:
    def Numbers(self, nums):
        return "\n".join([str(i) for i in nums.split()])
    def rerange(self, *args):
        if len(args) == 1:
            stop = args[0]
        elif len(args) == 2:
            stop = args[1]
            start = args[0]
        else:
            stop = args[1]
            start = args[0]
            step = args[2]
        return list(reversed([i for i in range(start, stop, step)]))



d = Mod()
print(d.rerange(0, 6, 3))

