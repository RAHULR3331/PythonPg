factorials_dict = {}

def factorial(n):
    if n in factorials_dict:
        return factorials_dict[n]
    elif n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n-1)
    factorials_dict[n] = result
    return result
print(factorial(5))
