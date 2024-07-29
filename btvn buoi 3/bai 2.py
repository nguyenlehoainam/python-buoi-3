k = int(input("Nhập số phần tử k: "))
a = [int(input(f"Nhập phần tử thứ {i + 1}: ")) for i in range(k)]
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if n * m > k:
    print("NO")
else:
    matrix = [a[i * m:(i + 1) * m] for i in range(n)]
    print("Ma trận nhận được là:")
    for row in matrix:
        print(row)