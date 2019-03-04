"""

Array sum iteration

class Array:
    def __init__(self, my_array=None):
        self.my_array = my_array

    def generate(self):
        self.my_array = int(input())

"""


def iteration_sum(num):
    elements_sum = 0
    for i in num:
        elements_sum = elements_sum + i
    return elements_sum


my_array = [1]
n = int(input('Enter how many elements you want: '))
for i in range(0, n):
    x = input('Enter the numbers into the array: ')
    my_array.append(int(x))
print('Array: ', my_array)
print(iteration_sum(my_array))
