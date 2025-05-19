class Shelf:
    def __init__(self, cnt=0, first=posx(0,0,0,0,0,0), interval=0, row=1, col=1):
        self.cnt = cnt
        self.first = first
        self.interval = interval
        self.stack = []
        self.row = row
        self.col = col
        self.build_stack()

    def build_stack(self):
        self.stack = []
        for i in range(self.row):       # 행: x 증가
            for j in range(self.col):   # 열: y 감소
                x = self.first[0] + i * self.interval
                y = self.first[1] - j * self.interval
                p = posx(x, y, self.first[2], self.first[3], self.first[4], self.first[5])
                self.stack.append(p)

    def get_cup_cord(self):
        if self.cnt == 0:
            tp_log("경고: 아이템이 없습니다.")
            return None
        return self.stack[self.cnt - 1]

    def push(self):
        if self.cnt >= len(self.stack):
            tp_log("경고: 선반이 가득 찼습니다.")
            return
        self.cnt += 1

    def pop(self):
        if self.cnt <= 0:
            tp_log("경고: 꺼낼 아이템이 없습니다.")
            return
        self.cnt -= 1


class CupShelf(Shelf):
    def __init__(self, cnt=0, first=posx(0,0,0,0,0,0), interval=0):
        super().__init__(cnt, first, interval, row=2, col=3)

class IceShelf(Shelf):
    def __init__(self, cnt=0, first=posx(0,0,0,0,0,0), interval=0):
        super().__init__(cnt, first, interval, row=3, col=3)

class MilkShelf(Shelf):
    def __init__(self, cnt=0, first=posx(0,0,0,0,0,0), interval=0):
        super().__init__(cnt, first, interval, row=1, col=3)

