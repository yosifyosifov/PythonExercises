orders=int(input())
total_price=0

for i in range(orders):
    price=float(input())
    days=int(input())
    capsules=int(input())
    order_price=price*days*capsules
    total_price +=order_price
    print(f'The price for the coffee is: ${order_price:.2f}')

print(f'Total: ${total_price:.2f}')