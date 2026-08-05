# constructor overloading
class Demo:
    def __init__(self):
        print("Hello ameesha")

    def __init__(self, a):
        print(a)

    def __init__(self, a, b, c):
        print(a, b, c)

# Demo()          # Invalid
# Demo(10)        # Invalid
Demo(100, 200, 300)   # Valid
