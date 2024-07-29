a = str(input('Nhập một chuỗi văn bản chứa họ và tên của một thành viên trong câu lạc bộ: '))
a1 = a.split()
for i in range(len(a)):
    print(a[i], end=" ")