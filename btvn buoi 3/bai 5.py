N = int(input('Nhập một số nguyên N ( 1 <= N <= 100): '))
my_list = [int(x) for x in input().split()]
dem = 0
new_list = []
if len(my_list) != N:
    print('Hãy nhập lại.')
else: 
    for i in range(len(my_list)):
        if my_list[i] % 2 == 1:
            dem += 1
            new_list.append(my_list[i])
print('có', dem, 'số thầy Ba thích trong các số Nasus có')
new_list.sort()
for num in new_list:
    print(num, end=" ")