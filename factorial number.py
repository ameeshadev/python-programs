#Factorial number
def factorial_number(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("Enter a number:"))
print("Factorial number is:",factorial_number(num))
