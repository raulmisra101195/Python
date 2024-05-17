s = 'python is very easy'
print(s.startswith('python'))
print(s.startswith('py'))
print(s.endswith('easy'))

s1 = 'python programming'
print(s1.removeprefix('py'))
print(s1.removeprefix('java'))
print(s1.removeprefix('ing'))

print(s.partition('is'))
print(s.partition('s'))
print(s.rpartition('s'))


s ='a-b-c-d-e'
print(s.replace('-',','))
print(s.replace('-',',',3))
print(s.replace('k','m'))

s = 'abce@gmail.com'
print(s.replace('gmail','yahoo'))


