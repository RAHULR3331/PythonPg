def reverse_num(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    while True:
        rev = reverse_num(n)
        total = n + rev
        if is_palindrome(total):
            return total
        n = total

num = int(input("Enter a number: "))
result = reverse_and_add(num)
print("Result:", result)
