num = int(input("Enter a number: "))
original_num = num
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

if original_num == reverse_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
