#smallest number
a = float(input("enter first number:"))
b = float(input("enter second number:"))
c = float(input("enter third number:"))
if (a<b) and (a<c):
    small=a
elif (b<a) and (b<c):
    small=b
else:
    small=c
print("the smallest number is",small)
