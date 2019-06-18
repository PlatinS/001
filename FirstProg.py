def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    fib(1000)
print("Hello world!")
a = 5
if a == 5:
    print('Равно 5!')
