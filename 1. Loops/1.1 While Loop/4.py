n = int(input('Enter a number  '))
counter = 0

while n > 0:
    n = n//10
    counter += 1

print("Number of Digits in counter are",counter)