n = int(input('Enter a number'))

bin = ''

while n > 0:
    r = n%2
    n = n//2
    bit = str(r) + bin

print(bin)