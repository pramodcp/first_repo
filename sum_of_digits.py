def sum_of_digit(n):
    total = 0
    while n != 0:
        total = total + (n % 10)
        n = n // 10
    return total

n = int(input('Enter a number: '))
x = sum_of_digit(n)
print(f"Sum of Digits of a given number is {x}")
#print(f"Sum of Digits of a given number is {sum_of_digit(num)}")