a=int(input("enter first number:"))
b=int(input("enter second number:"))
def sumOrProd(x,y):
    if x*y<=1000:
        print("product:",x*y)
    else:
        print("sum:",x+y)
sumOrProd(a,b)

