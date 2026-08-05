# Write a Python code to find the maximum element in the list of elements.

class Sum:
    def findsum_max(self, arr):
        maximum = arr[0]
        minimum = arr[0]

        for i in arr:
            if i > maximum:
                maximum = i
            elif i < minimum:
                minimum = i

        return maximum + minimum

a = [10, 20, 30, 40, 89, 76, 50]
b = Sum()
print(b.findsum_max(a))
