def fibonacci_series(n):
    num1 = 0
    num2 = 1

    for i in range(n):
        print(num1, end=" ")
        result = num1 + num2
        num1 = num2
        num2 = result

n = int(input("Enter a number: "))
fibonacci_series(n)
