n = int(input("Give me a number: "))

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

output = factorial(n)
print(f"The factorial of {n} is {output}")
    
