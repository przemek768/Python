def numbers(n: int):
    if n < 0:
        return
    for n in range(n, -1, -1):
        print(n)
        print("\n")
        n = n - 1

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def power(number: int, n: int) -> int:
    pom = 0
    for pom in range(0, n-1, 1):
        number = number * number
    return number

def reverse(txt: str) -> str:
    return txt[::-1]

def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

def prime(n: int) -> bool:


numbers(15)
print("fib"+"\n")
print(fib(20))
print("power"+"\n")
print(power(2, 4))
print("reverse"+"\n")
txt_help = "ala ma kota"
print(reverse(txt_help))
print("factorial"+"\n")
print(factorial(4))


