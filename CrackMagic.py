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
        self.c_dict_l = len(c_dict)
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

        pw_l = len(self.pw)

        if self.c_dict_l:
            for p_len in range(1, 9):
                for g in itertools.product(self.c_dict[self.y], repeat=p_len):
                    self.i += 1
                    g = "".join(g)

                    if g == self.pw[self.x]:
                        self.c_pw += "".join(g)
                        self.y = 0
                        self.x += 1
                        # print("%s %s (Hit!!!)" % (g, self.i))

                        if(pw_l == self.x):
                            e = timer()
                            print("Password: %s \nTime Elapsed: %s"
                                  % (self.c_pw, e - self.s))
                            self.x = 0
                            self.c_pw = ''
                            return True

                        return self.attemptCrack(self.pw)
                    # print(g, self.i)

                self.y += 1

                if(self.y != c_dict_l):
                    return self.attemptCrack(self.pw)
                else:
                    print("Aborted! A character is not in dictionary!")
                    return False


c = CrackMagic()
c.attemptCrack('Ms9at')
c.attemptCrack('^a%')
