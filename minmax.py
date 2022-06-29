class Minmax:

    def __init__(self,arr):
        self.arr = arr

    def compare(self, x, y, mx, mi):
        if x > y:
            mx = max(mx, x)
            mi = min(mi, y)
        else:
            mx = max(mx, y)
            mi = min(mi, x)
        return mx,mi

    def lst(self):
        a = list(map(int, self.arr.split()))
        return a

    def calculate(self):
        if len(self.lst()) % 2 == 0:
            i = 2
            mx = max(self.lst()[0], self.lst()[1])
            mi = min(self.lst()[0], self.lst()[1])
            while i < len(self.lst())-1:
                mx, mi = self.compare(self.lst()[i], self.lst()[i+1], mx, mi)
                i += 2
        else:
            i = 1
            mx = self.lst()[0]
            mi = self.lst()[0]
            while i < len(self.lst())-1:
                mx, mi = self.compare(self.lst()[i], self.lst()[i+1], mx, mi)
                i += 2
        return mx, mi


minmax = Minmax(input("input\n"))
maxi, mini = minmax.calculate()
print(f"max is {maxi}\nmin is {mini}")
