def f(money, interest, month):
    return money*pow((1+0.01*interest), month)

print(f(1000, 10, 12))