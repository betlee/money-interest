money = int(input())
interest = int(input())
month = int(input())
def f(money, interest, month):
    return money*pow((1+0.01*interest), month)

print(f(money, interest, month))