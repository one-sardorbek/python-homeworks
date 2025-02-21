def invest(amount, rate, years):
    for i in range(1, years+1):
        amount=amount + amount * (rate/100)
        print("year ",i,": ",amount)
a,r,y=map(int,input().split())
invest(a,r,y)