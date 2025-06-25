i = int(input("son kiriting: "))
n = int(input("son nechigacha bolsin"))

for num in range (i, n+1):
    print(num, end="." if num<n else "" )