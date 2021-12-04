import functools

report = []
REPORTFILE = "..\\4.txt"
with open(REPORTFILE, 'r') as f:
    report = f.readlines()
report_len = len(report)

numbers = report.pop(0)[:-1].split(',')
numbers = [int(n) for n in numbers]
report = [b[:-1] for b in report] # clean up \n

class Card:
    def __init__(self) -> None:
        self.numbers = []
        self.markers = [[False] * 5 for i in range(5)]
    def do_number(self, number):
        for r in range(len(self.numbers)):
            for n in range(len(self.numbers[r])):
                if number == self.numbers[r][n]:
                    self.markers[r][n] = True
    def check_bingo(self) -> bool:
        col_checker = [True] * 5
        for r in range(len(self.numbers)):
            if functools.reduce(lambda x, y: x and y, self.markers[r]):
                return True
            col_checker = [x and y for x, y in zip(col_checker, self.markers[r])]
        if True in col_checker:
            return True
        return False
    def result(self, num):
        sum = 0
        for r in range(len(self.numbers)):
            for n in range(len(self.numbers[r])):
                if not self.markers[r][n]:
                    sum += self.numbers[r][n]
        return sum * num
    def __repr__(self) -> str:
        s = ''
        for r in self.numbers:
            s += str(r) + '\n'
        for r in self.markers:
            s += str(r) + '\n'
        return s

# repr cards as 2d array of tuples
cards: list[Card] = []
for s in report:
    if s == '':
        cards.append(Card())
    else:
        cards[-1].numbers.append(list(map(int, s.split())))

def run1():
    for n in numbers:
        for i in range(len(cards)):
            cards[i].do_number(n)
            if cards[i].check_bingo():
                print(f'result: {cards[i].result(n)}')
                return
            
run1()

def run2():
    # card, number of numbers to get bingo, last number drawn once gets bingo
    last = (Card(), 0, 0)
    for card in cards:
        for i in range(len(numbers)):
            n = numbers[i]
            card.do_number(n)
            if card.check_bingo():
                if i > last[1]:
                    last = (card, i, n)
                break
    print(f'result part 2: {last[0].result(last[2])}')
    return
run2()
