import re

class PhoneNumber:
    def __init__(self, number):
        self.number_to_check = number
        self.check_number()

    def check_number(self):
        if re.search('[a-zA-Z]', self.number_to_check):
            raise ValueError('letters not permitted')
        if re.search('[:@!]', self.number_to_check):
            raise ValueError('punctuations not permitted')
        
        self.number = re.sub("[^0-9]", "", self.number_to_check)

        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.number) == 11:
            if self.number[0] != "1":
                raise ValueError("11 digits must start with 1")
            self.number = self.number[1:]
        
        self.number = self.number
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.end_number = self.number[6:]

        if self.area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if self.area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if self.exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")
        
    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.end_number}"
        
