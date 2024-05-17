Psum = 0 
Nsum = 0
count = 0
num_of_nos = int(input('ENter number of input  '))
max = int(input('Enter a num '))
while count < num_of_nos:
    n = int(input('Enter number '))
    if n > max:
        max = n
    count = count + 1
print('Max number is', max)