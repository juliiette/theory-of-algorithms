"""

Array sum recursion

"""

my_array = [1]
n = int(input('Enter how many elements you want: '))
for i in range(0, n):
    x = input('Enter the numbers into the array: ')
    my_array.append(int(x))
print('Array: ', my_array)

def recursion_sum(my_array):
    if len(my_array) == 1:
        return my_array[0]
    else:
        return my_array[0] + recursion_sum(my_array[1:])


print(recursion_sum(my_array))
