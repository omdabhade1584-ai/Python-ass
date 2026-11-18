n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i + 1}: ")))

unique = []

for element in arr:
    if element not in unique:
        unique.append(element)

print("Original array:", arr)
print("Array after removing duplicates:", unique)