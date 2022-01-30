from ast import operator


print('SIMPLE CALCULATOR')
first_number = input('Enter First Number ')

if first_number.isnumeric()==False:        #isnumeric() checks where the first_number is numerical value or not
    print('Please enter a valid number.')
    exit()

operation = input('Enter Operator ')
second_number = input('Enter Second  Number ')

if second_number.isnumeric() == False:   
    print('Please enter a valid number.')
    exit()

first_number = int(first_number)       # as numeric value contains float or integer or double, so casting it to integer
second_number = int(second_number)
result=0

if operation == '+':
    result= first_number + second_number
    label = 'sum'
elif operation == '-':
    result= first_number - second_number
    label = 'difference'
elif operation == '*':
    result= first_number * second_number
    label = 'product'
elif operation == '/':
    result= first_number / second_number
    label = 'division'
elif operation == '**':
    result= first_number ** second_number
    label = 'exponential'
elif operation == '%':
    result= first_number % second_number
    label = 'modulus'
else:
    print('Operation not recognized')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' is ' + str(result))
