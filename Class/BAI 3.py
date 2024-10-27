class ToanHoc:
    def __init__(self, nSo):
        self.nSo=nSo

    def Sum(self, nSo):
        sumNSo=0
        for x in nSo:
            sumNSo+=x

        return sumNSo

    def Avg(self, nSo):
        return self.Sum(nSo)/len(nSo)

    def Max(self, nSo):
        Max=-9999999999
        [Max := x for x in nSo if Max < x]
        return Max

    def Min(self, nSo):
        Min=9999999999
        [Min := x for x in nSo if Min > x]
        return Min

    def Print(self):
        print("So luong cac so trong thanh phan du lieu: ", len(self.nSo))
        print("Cac so trong thanh phan du lieu la: ", end = '')
        [print(x, end = ' ') for x in self.nSo]    
        print("\nTong n so: ", self.Sum(self.nSo))
        print("Trung binh cong cua n so: ", self.Avg(self.nSo))
        print("So lon nhat trong n so: ", self.Max(self.nSo))
        print("So be nhat trong n so: ", self.Min(self.nSo))

numbers=[10, 9, 12, 14, 16, 20, 25]
math=ToanHoc(numbers)
math.Print()