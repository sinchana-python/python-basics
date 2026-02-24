print("enter a number:")
n=int(input())
if n % 2 == 0:
    print("even")
else:
    print("odd")

print("enter a number:")
number=int(input())
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

print("enter two numbers:")
a=int(input())
b=int(input())
if a>b:
    print("largest =,a")
if b>a:
     print("largest =,b")