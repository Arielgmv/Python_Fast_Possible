# Exercise 2: Print the sum of the current number and the previous number
"""
print("Printing current and previous number and their sum in a range(10)")
for i in range(0, 10):
    current = i
    previous = i-1
    sum = current + previous
    if current==0:
        previous=0
        sum = current + previous
        print('Current Number', current, 'Previous Number', previous, 'Sum', sum)    
    else:
        print('Current Number', current, 'Previous Number', previous, 'Sum', sum)
    #print('Previous Number', previous)
    #print('Sum', sum)
"""
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print('Current Number', i, 'Previous Number', previous_num, 'Sum: ', x_sum)    
    # modify previous number
    # set it to the current number
    previous_num = i
    