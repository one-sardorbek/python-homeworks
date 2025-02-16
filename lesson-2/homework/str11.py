a=input()
digits=["0","1","2","3","4","5","6","7","8","9"]
n=0
for i in range(len(a)):
    if a[i] in digits:
        n+=1
if n>0:
    print("yes")
else:
    print("no")
