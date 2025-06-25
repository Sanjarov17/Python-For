first = int(input()) 
arzon_price = first
qimmat_price = first

for _ in range(4):
    price = int(input())
    if price < arzon_price:
        min_price = price
    if price > qimmat_price:
        qimmat_price = price

print(arzon_price, ",", qimmat_price)