import math


class learnBasicPython:

    def __init__(self, name, inClass):
        self.name = name
        self.inClass = inClass

    # xem sinh nhat cua ban be
    # su dung if, else, array, for, json, input
    def showBirthDay(self):
        birthdays = {
            'Tang Ba Hong Phuc': '29/06/2000',
            'Nguyen Van Cuong': '01/02/2000',
            'Nguyen Huu Cuong': "04/05/1999",
            'Ho Hoang Hau': "30/06/2000"
        }
        print('My friends: ')
        for name in birthdays:
            print(name)

        print('who do you want show the birthday?')
        name = input()

        if name in birthdays:
            print(f'{name}\'s birthday is {birthdays[name]}')
        else:
            print(f'Sadly, we don\'t have {name}\'s birthday.')

    # tìm ước của số cho trước
    # su dung if, array(extend) , for, abs
    def timUoc(self):
        try:
            number = int(input("Enter num:"))
        except ValueError:
            print("Vui long nhap so nguyen")
            exit(0)
        # or
        # if not type(number) is int:
        #     raise TypeError("Only integers are allowed")
        # or
        # if not type(number) is int:
        #     raise Exception("Sorry, no numbers below zero")
        #

        if number == 0:
            print("So 0 khong co uoc")
            exit(0)
        array = []
        for i in range(1, abs(number) + 1):
            if number % i == 0:
                array.extend([i])
        print(array)

    # tinh giá trị của biểu căn(2*c*d/h)
    # su dung expression của array list, sqrt
    def caclulator(self):
        c = 50
        h = 30
        value = []
        items = [x for x in input("Nhập giá trị của d: ").split(',')]
        for d in items:
            value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
        print(','.join(value))






