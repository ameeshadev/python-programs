 # counting number of digits in a number
def count_digit(n):
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count
n=int(input("Enter a number:"))
print("Number of digits:",count_digit(n))
