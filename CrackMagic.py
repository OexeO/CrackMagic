import itertools
import string
import sys
from timeit import default_timer as timer


class CrackMagic:

    def __init__(self,
                 x=0, y=0, i=0,
                 c_pw='', pw='',
                 c_dict=[string.printable, '0123456789'],
                 s=timer()):
        self.x = x
        self.y = y
        self.i = i
        self.c_pw = c_pw
        self.pw = pw
        self.c_dict = c_dict
        self.s = s

    def getCrackDict(self):
        return self.c_dict

    def setCrackDict(self, c_dict):
        self.c_dict = c_dict

    def addCrackDict(self, c_dict):
        self.c_dict.append(c_dict)

    def getGuessCount(self):
        return self.i

    def getSource(self):
        return self.pw

    def setSource(self, pw):
        self.pw = pw

    def attemptCrack(self, pw):
        if pw:
            self.pw = pw
        for p_len in range(1, 9):
            for g in itertools.product(self.c_dict[self.y], repeat=p_len):
                self.i += 1
                g = ''.join(g)
                if g == self.pw[self.x]:
                    self.c_pw += ''.join(g)
                    self.y = 0
                    self.x += 1
                    print(g, str(self.i), " (Hit!!!)")
                    if(len(self.pw) == self.x):
                        e = timer()
                        print("Password:", self.c_pw,
                              "\nTime Elapsed:", str(e - self.s))
                        return self.c_pw, str(e - self.s)
                    return self.attemptCrack(self.pw)
                print(g, str(self.i))
            self.y += 1
            if(self.y != len(self.c_dict)):
                return self.attemptCrack(self.pw)
            else:
                print("Aborted! A character is not in dictionary!")
                sys.exit()


c = CrackMagic()
print(c.attemptCrack('C%s6'))
