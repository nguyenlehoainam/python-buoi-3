s1 = str(input('Nhập vào chuỗi s1: '))
s2 = str(input('Nhập vào chuỗi s2: '))
print(s1[::-1])
a = int(input())
b = int(input())
if 1 <= a < b < len(s2):
    print(s2[:a-1] + s2[a-1:b][::-1] + s2[b:])
s3 = ''
for i in range(len(s1)):
    if i % 2 == 1:
        s3 += s1[i]
print(s3)
s4 = ''
for i in range(len(s1) + len(s2)):
    if i < len(s1):
        s4 += s1[i]
    if i < len(s2):
        s4 += s2[i]
print(s4)
print(s2[:2] + s1[2:])
print(s1[:2] + s2[2:])