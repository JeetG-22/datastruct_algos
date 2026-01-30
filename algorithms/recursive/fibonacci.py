n = int(input("Give me a number: "))

def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

output = fibonacci(n)
print(f"The {n}th number in fibonacci is {output}")
    
