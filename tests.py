from solution import File

test3 = File('D:/tests3.txt')
test2 = File('D:/test2.txt')
# f2.write('f2')
a = test3 + test2
print(f'f = {test3.read()}', type(test3))
print(f'f2 = {test2.read()}', type(test2))
print(f'a = {a.read()}', type(a))
print(test2.read())

# for i in f:
#     print(i)