n = int(input())  # Foydalanuvchi n ni kiritadi

juft = 0  # juftlar yig'indisi
toq = 0  

for i in range(1, n + 1):
    if i % 2 == 0:
        juft += i
    else:
        toq += i

print(juft, ",", toq)