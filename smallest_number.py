#smallest number
a = eval(input("enter first number:"))
b = eval(input("enter second number:"))
c = eval(input("enter third number:"))
if (a<b) and (a<c):
    small=a
elif (b<a) and (b<c):
    small=b
else:
    small=c
print(f"The smallest number is {small} from given number {a},{b},{c}")
