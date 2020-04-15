import math as m
import collections as coll

def Summ(a, l):
    num = ''
    for i in range(0,l):
        a *= 2.0
        num += str(m.trunc(a))
        if a >= 1.0:
            a -= 1.0
    return num

class Coder:
    text = ''
    code = ''
    wordNew = {}
    deWord = {}
    def Coder(self):
        sum = 0.0
        for i in self.text:
            if i not in self.wordNew:
                self.wordNew[i.lower()] = [1, 0, 0, '']
            else:
                self.wordNew[i][0] += 1
        self.wordNew = coll.OrderedDict(sorted(self.wordNew.items(),key = lambda i:i[0]))
        for i in self.wordNew:
            self.wordNew[i][0] /=  len(self.text)
            self.wordNew[i][1] = m.ceil(m.log2(1 / self.wordNew[i][0])) + 1
            self.wordNew[i][2] = self.wordNew[i][0] / 2 + sum
            self.wordNew[i][3] = Summ(self.wordNew[i][2], self.wordNew[i][1])
            sum += self.wordNew[i][0]
        for i in self.text.lower():
            self.code += self.wordNew[i][3]
        print(self.code)
    def Decoder(self):
        for k, i in self.wordNew.items():
            self.deWord[i[3]] = k
        w = ''
        for i in self.code:
            try:
                w += i
                print(self.deWord[w], end='')
                w = ''
            except:
                pass
c = Coder()
c.text = input()
c.Coder()
c.Decoder()
s = 0.0
h = 0.0
for i in c.text.lower():
    s += c.wordNew[i][0] * c.wordNew[i][1]
    h += c.wordNew[i][0] * m.log2(1 / c.wordNew[i][0])
print('\n', s, sep='')
print(h + 2)