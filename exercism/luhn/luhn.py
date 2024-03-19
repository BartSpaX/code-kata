class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        new_num = self.card_num
        if len(self.card_num) <= 1:
            return False
        if not self.card_num.isnumeric():
            return False
        total = sum(int(num) for num in new_num[-1::-2])
        for num in new_num[-2::-2]:
            num = int(num) * 2
            total += num if num < 9 else num - 9
        return total % 10 == 0
