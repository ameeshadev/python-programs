# Write a Python code to find the maximum element in the list of elements.

class Maximum:
    def find_max(self, arr):
        maximum = arr[0]
        for i in arr:
            if i > maximum:
                maximum = i
        return maximum

a = [10, 20, 30, 40, 89, 76, 50]
b = Maximum()
print(b.find_max(a))
