def check(func):
    def wrapper(a,b):
        try:
            a=func(a,b)
        except ZeroDivisionError:
           a="Denominator can't be zero"
        return a
    return wrapper
@check
def div(a, b):
   return a / b
a,b=map(int,input().split())
print(div(a,b))

