n = int(input("Nechta son kiritasiz: "))
first = int(input()) 
max_val = first
min_val = first

for _ in range(n - 1):
    num = int(input())
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

average = (max_val + min_val) / 2
print(average)