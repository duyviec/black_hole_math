__author__ = 'vlmduy'

import re

def receive_input():
    flag = True
    while flag:
        print('Please input any number: ')
        data = raw_input()
        if re.match(r'^[0-9]+$', data):
            list_num = [n for n in data]
            for num in list_num:
                if list_num.count(num) > (len(data) - 2):
                    print('Each number must not appear more than ' + str(len(data) - 1))
                    flag = True
                    break
            else:
                flag = False
    data = [n for n in data]
    number = ''.join(data)
    get_black_hole_number(number)


def get_black_hole_number(number):
    flag = True
    while flag:
        print "Input: " + str(number)
        decrease_num = sorted(number, reverse=True)
        increase_num = sorted(number, reverse=False)
        subtract = int(str(''.join(decrease_num))) - int(str(''.join(increase_num)))
        print "Largest: " + str(''.join(decrease_num))
        print "Smallest: " + str(''.join(increase_num))
        print "Largest - Smallest: " + str(subtract)
        if subtract == int(number):
            flag = False
            print "You have reach the black hole of " + str(len(number)) + " numbers: " + str(subtract)
        else:
            number = str(subtract)

if __name__ == "__main__":
    receive_input()