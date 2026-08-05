class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size
        print(self.size)

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return temp

    def IsEmpty(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def IsFull(self):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            print("Stack is not full")

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

obj = Stack(5)

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    data = list(map(int, input("Enter elements: ").split()))
    obj.push(data)

elif choice == 2:
    print("Popped element:", obj.pop())

elif choice == 3:
    obj.IsEmpty()

elif choice == 4:
    obj.IsFull()

elif choice == 5:
    obj.display()

else:
    print("Invalid Choice")
