class Revarr:

    def __init__(self, arr):
        self.arr = arr

    def cal_rev_str(self):  # for normal string
        s = self.arr
        r = ''
        for i in range(1, len(s)+1):
            r += s[-i]
        return r

    def cal_rev_list(self):  # for string in list
        s = self.arr
        start = 0
        end = len(s)-1
        while start<end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
    def cal_rev(self):
        if type(self.arr) is list:
            return self.cal_rev_list()
        else:
            return self.cal_rev_str()


print("what is your output format \n 1. for list \n 2. for normal string")
num = int(input("enter num.\n"))
if num == 2:
    word = Revarr(input('input\n'))
    print(word.cal_rev())
else:
    string = list(map(str, input('input\n')))
    word = Revarr(string)
    print(word.cal_rev())
